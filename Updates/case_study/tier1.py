from __future__ import division
import sys
import json
import time
#from queue import Queue
from collections import deque
from sets import Set

f = sys.argv[1] #the topology file
f2 = sys.argv[2] #the tor file

# use dictionary to save the as relationships
# asdict[asn] = [[provider-customer edges],[peer-to-peer edges],[customer-provider edges]]
# use BFS to traverse the graph from a source AS
# graph[node] = [weight, equal_paths, uphill_hops]

asdict = {}
graph = {}
tordict = {} # tor dictionary to record resilience of each Tor AS
torpath = {} # tor dictionary to record customer-provider and unreachable nodes to each Tor AS

with open(f,'r') as fin:
    for line in fin:
        arr = line.split('|')
        asn1 = arr[0].strip()
        asn2 = arr[1].strip()
        rel = int(arr[2].strip()) # -1: provider-customer; 0: peer-to-peer
        if asdict.has_key(asn1):
            asdict[asn1][rel+1].append(asn2)
        else:
            asdict[asn1] = [[],[],[]]
            asdict[asn1][rel+1] = [asn2]
        if asdict.has_key(asn2):
            asdict[asn2][abs(rel)+1].append(asn1)
        else:
            asdict[asn2] = [[],[],[]]
            asdict[asn2][abs(rel)+1] = [asn1]

total_as = len(asdict)
print total_as

with open(f2,'r') as fin:
    for line in fin:
        asn = line.strip()
        tordict[asn] = 0
        torpath[asn] = (Set([]), Set([])) # tup: (cp set, unreachable set)

# initialize graph
def init(root):
    graph = {}
    graph[root] = [0,1,0]
    return graph

# provider to customer
def bfs_pc(q_lst):
    q = deque(q_lst)
    while q:
        current = q.popleft()
        val = graph[current]
        for node in asdict[current][0]:
            if not graph.has_key(node):
                graph[node] = [val[0] + 1, val[1], val[2]]
                q.append(node)
            elif graph[node][0] == val[0] + 1:
                graph[node][1] += val[1]

# peer to peer
def bfs_pp(q_lst):
    q = deque()
    for rt in q_lst:
        for node in asdict[rt][1]:
            if not graph.has_key(node):
                # NOTE: the total_as below used to be 53000, an artificial number that's > total_as.
                graph[node] = [graph[rt][0] + total_as, graph[rt][1], graph[rt][2]]
                q.append(node)
            elif graph[node][0] == graph[rt][0] + total_as:
                graph[node][1] += graph[rt][1]
    while q:
        current = q.popleft()
        val = graph[current]
        for node in asdict[current][0]:
            if not graph.has_key(node):
                graph[node] = [val[0] + 1, val[1], val[2]]
                q.append(node)
            elif graph[node][0] == val[0] + 1:
                graph[node][1] += val[1]

# customer to provider
def bfs_cp(root):
    q = deque()
    q.append(root)
    curlst = []
    curlevel = 0
    while q:
        current = q.popleft()
        val = graph[current]
        if val[2] > curlevel:
            bfs_pc(curlst)
            bfs_pp(curlst)
            curlst = []
            curlevel = val[2]
        for node in asdict[current][2]:
            if not graph.has_key(node):
                graph[node] = [val[0], val[1], val[2] + 1]
                q.append(node)
                curlst.append(node)
            elif graph[node][2] == (val[2]+1):
                graph[node][1] += val[1]

# traverse nodes to calculate resiliency
def update_resilience(root):
    L = sorted(graph.items(), key=lambda(k,v): (v[2],v[0])) # order by preference high to low
    L2 = map(lambda (k,v): k, L)
    #================
    #only cares about tier 1 ASes
    #================
    nodes = []
    prev = ()
    eq_path = 0
    eq_nodes = []
    buffer = []
    # traverse the preference list
    for item in L2:
        if item in tier1_lst:
            val = graph[item]
            if prev==(val[0],val[2]):
                eq_path += val[1]
                eq_nodes.append(item)
                if tordict.has_key(item):
                    buffer.append((item,val[1]))
            else:
                num_traversed = len(tier1_lst) - len(nodes) - len(eq_nodes)
                if root in tier1_lst:
                    num_traversed -= 1
                for node in buffer:
                    cp_set = torpath[node[0]][0]
                    unreach_set = torpath[node[0]][1]
                    #check for unreachability
                    num_unreach = len(unreach_set & Set(nodes))
                    #check for customer-provider
                    set_cp = cp_set & Set(nodes)
                    for i in set_cp:
                        if graph[i][0] not in [0, total_as]:
                            num_unreach += 1
                    # take care of equal nodes
                    frac = 0
                    if node in eq_nodes:
                        if len(eq_nodes) > 1:
                            eq_nodes.remove(node[0])
                            set_unreach = unreach_set & Set(eq_nodes)
                            set_cp = cp_set & Set(eq_nodes)
                            for i in set_cp:
                                if graph[i][0] not in [0, total_as]:
                                    set_unreach.add(i)
                            if len(set_unreach) == len(eq_nodes):
                                frac = len(eq_nodes)
                            else:
                                counter_paths = sum([graph[i][1] for i in set_unreach])
                                frac = len(set_unreach) + (node[1] / (eq_path - counter_paths))
                            eq_nodes.append(node[0])
                    else:
                        set_unreach = unreach_set & Set(eq_nodes)
                        frac = len(set_unreach)
                        if (graph[node[0]][0],graph[node[0]][2]) == prev:
                            counter_paths = sum([graph[i][1] for i in set_unreach])
                            frac += node[1] / (eq_path + node[1] - counter_paths)
                    tordict[node[0]] += num_traversed + num_unreach + frac
                
                buffer = []
                nodes += eq_nodes
                eq_path = val[1]
                eq_nodes = [item]
                prev = (val[0],val[2])
                if tordict.has_key(item):
                    buffer = [(item,val[1])]
        else:
            if tordict.has_key(item):
                buffer.append((item,graph[item][1]))
    # leftover nodes in buffer
    num_traversed = len(tier1_lst) - len(nodes) - len(eq_nodes)
    if root in tier1_lst:
        num_traversed -= 1
    for node in buffer:
        cp_set = torpath[node[0]][0]
        unreach_set = torpath[node[0]][1]
        #check for unreachability
        num_unreach = len(unreach_set & Set(nodes))
        #check for customer-provider
        set_cp = cp_set & Set(nodes)
        for i in set_cp:
            if graph[i][0] not in [0, total_as]:
                num_unreach += 1
        # take care of equal nodes
        frac = 0
        if node in eq_nodes:
            if len(eq_nodes) > 1:
                eq_nodes.remove(node[0])
                set_unreach = unreach_set & Set(eq_nodes)
                set_cp = cp_set & Set(eq_nodes)
                for i in set_cp:
                    if graph[i][0] not in [0, total_as]:
                        set_unreach.add(i)
                if len(set_unreach) == len(eq_nodes):
                    frac = len(eq_nodes)
                else:
                    counter_paths = sum([graph[i][1] for i in set_unreach])
                    frac = len(set_unreach) + (node[1] / (eq_path - counter_paths))
                eq_nodes.append(node[0])
        else:
            set_unreach = unreach_set & Set(eq_nodes)
            frac = len(set_unreach)
            if (graph[node[0]][0],graph[node[0]][2]) == prev:
                counter_paths = sum([graph[i][1] for i in set_unreach])
                frac += node[1] / (eq_path + node[1] - counter_paths)
        tordict[node[0]] += num_traversed + num_unreach + frac


# Calculate set of nodes using customer-provider paths to each Tor AS
def calc_torpath():
    for item in torpath:
        if asdict.has_key(item):
            bfs_graph = {}
            bfs_graph[item] = 1 #node item has been traversed
            q = deque()
            q.append(item)
            cp_set = Set([]) #set of nodes using c-p path to Tor AS
            unreach_set = Set([])
            #add customer-provider edges
            while q:
                current = q.popleft()
                for node in asdict[current][2]:
                    if not bfs_graph.has_key(node):
                        bfs_graph[node] = 1
                        q.append(node)
            #add peer-peer edge
            for i in bfs_graph.keys():
                q.append(i)
                for node in asdict[i][1]:
                    if not bfs_graph.has_key(node):
                        bfs_graph[node] = 1
                        q.append(node)
            #add provider-customer edges
            while q:
                current = q.popleft()
                for node in asdict[current][0]:
                    if not bfs_graph.has_key(node):
                        bfs_graph[node] = 1
                        q.append(node)
                        cp_set.add(node)
            #calc unreachable set
            unreach_set = Set(asdict.keys()) - Set(bfs_graph.keys())
            torpath[item] = (cp_set, unreach_set)



#======================Prepare list of source ASes=======================#

#toplst = ['6128','25019','8972','6893','15467','32613','30058','174','47069','26347','12880','5384','4766','558','20773','2497','34400','7992','41495','23393','44244','13768','5607','8404','33668','2518','3356','20542','29873','12015','10929','3595','8447','2840','36827']
#print len(toplst)
#check existence
#for item in toplst:
#    if not asdict.has_key(item):
#        toplst.remove(item)
#        print item
#keys = asdict.keys()
#toplst = random.sample(keys,1000)
#print len(toplst)

#Top 20 client ASes
#toplst =['6128','25019','8972','6893','15467','32613','30058','174','47069','26347','12880','5384','4766','558','20773','2497','34400','7992','41495','23393']

#Tor client ASes that also contain Tor relays
# 6128, 8972, 6893, 30058, 174, 4766, 20773
# ['6128', '8972', '6893', '30058', '174', '4766', '20773']

#sys.exit(1)


#======================Prepare list of Intercepting ASes: Tier1 ASes=======================#

# Tier 1 ASes: 17 ASes here
tier1_lst = ['174','209','286','701','1239','1299','2828','2914','3257','3320','3356','5511','6453','6461','6762','7018','12956']


#==========Prepare list of cp and unreachable nodes to each Tor AS========#

start = time.time()

calc_torpath()

end = time.time()
print end - start

#sys.exit(1)


#===============Main part: calc resiliency from all source nodes===========#
start = time.time()

#counter = 9
for item in asdict:
    #print "===========%s" % item
    graph = init(item)
    bfs_pc([item])
    bfs_pp([item])
    bfs_cp(item)
    graph.pop(item,None)
    update_resilience(item)
    #print tordict
    #if counter <= 0:
    #    break
    #else:
    #    counter -= 1

end = time.time()
print end - start


#===============Normalize the Results to [0,1]===============#

with open('raw.json', 'w+') as fp:
    json.dump(tordict, fp)

for item in tordict:
    divid_tier = len(tier1_lst)
    #divid_top = len(toplst)
    if item in tier1_lst:
        divid_tier -=1
    #if item in toplst:
    #    divid_top -= 1
    tordict[item] = tordict[item] / (divid_tier * (total_as - 2))

with open('data.json', 'w+') as fp:
    json.dump(tordict, fp)

