from __future__ import division
import sys
import json
import time
#from queue import Queue
from collections import deque

f = sys.argv[1] #the topology file
f2 = sys.argv[2] #the tor file

# use dictionary to save the as relationships
# asdict[asn] = [[provider-customer edges],[peer-to-peer edges],[customer-provider edges]]
# use BFS to traverse the graph from a source AS
# graph[node] = [weight, equal_paths, uphill_hops]

asdict = {}
graph = {}
tordict = {}

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
#print total_as

with open(f2,'r') as fin:
    for line in fin:
        asn = line.strip()
        tordict[asn] = 0

# initialize graph
def init(root):
    graph = {}
    graph[root] = [0,1,0]
    return graph

# provider to customer
def bfs_pc(q_lst):
    #q = Queue()
    #q.put(root)
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
    #q = Queue()
    q = deque()
    for rt in q_lst:
        for node in asdict[rt][1]:
            if not graph.has_key(node):
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
    #q = Queue()
    #q.put(root)
    q = deque([root])
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
    #print L2
    #unreachable = total_as - 1 - len(L2)
    #print "number of unreachable nodes is %i" % unreachable
    #================
    #only cares about tier 1 ASes
    #================
    nodes = 0
    prev = ()
    eq_path = 0
    eq_nodes = []
    buffer = []
    for item in L2:
        if item in tier1_lst:
            val = graph[item]
            if prev==(val[0],val[2]):
                eq_path += val[1]
                eq_nodes.append(item)
                if tordict.has_key(item):
                    buffer.append((item,val[1]))
            else:
                num_traversed = len(tier1_lst) - nodes - len(eq_nodes)
                if root in tier1_lst:
                    num_traversed -= 1
                for node in buffer:
                    frac = 0
                    if node[0] in eq_nodes:
                        if len(eq_nodes) > 1:
                            frac = node[1] / eq_path
                    else:
                        if (graph[node[0]][0],graph[node[0]][2]) == prev:
                            frac = node[1] / (eq_path + node[1])
                    tordict[node[0]] += num_traversed + frac

                buffer = []
                nodes += len(eq_nodes)
                eq_path = val[1]
                eq_nodes = [item]
                prev = (val[0],val[2])
                if tordict.has_key(item):
                    buffer = [(item,val[1])]
        else:
            if tordict.has_key(item):
                buffer.append((item,graph[item][1]))
    # leftover nodes in buffer
    num_traversed = len(tier1_lst) - nodes - len(eq_nodes)
    if root in tier1_lst:
        num_traversed -= 1
    for node in buffer:
        frac = 0
        if node[0] in eq_nodes:
            if len(eq_nodes) > 1:
                frac = node[1] / eq_path
        else:
            if (graph[node[0]][0],graph[node[0]][2]) == prev:
                frac = node[1] / (eq_path + node[1])
        tordict[node[0]] += num_traversed + frac


#======================Prepare list of Intercepting ASes: Tier1 ASes=======================#

# Tier 1 ASes: 17 ASes here
tier1_lst = ['174','209','286','701','1239','1299','2828','2914','3257','3320','3356','5511','6453','6461','6762','7018','12956']

#===============Main part: calc resiliency from all source nodes===========#

#start = time.time()

#counter = 99
for item in asdict:
    #print "item is %s =========" % item
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

#end = time.time()
#print end - start

#normalize the resiliency data to [0,1]
#divid = (total_as - 2) * (total_as - 1)
for item in tordict:
    divid_tier = len(tier1_lst)
    if item in tier1_lst:
        divid_tier -= 1
    tordict[item] = tordict[item] / (divid_tier * (total_as - 2))

with open('test.json', 'w+') as fp:
    json.dump(tordict, fp)



