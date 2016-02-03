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
def update_resilience():
    L = sorted(graph.items(), key=lambda(k,v): (-v[2],-v[0]))
    L2 = map(lambda (k,v): k, L)
    #print L2
    unreachable = total_as - 1 - len(L2)
    #print "number of unreachable nodes is %i" % unreachable
    nodes = 0
    prev = ()
    eq_path = 0
    eq_nodes = 0
    buffer = []
    for item in L2:
        val = graph[item]
        if prev==(val[0],val[2]):
            eq_path += val[1]
            eq_nodes += 1
            if tordict.has_key(item):
                buffer.append((item,val[1]))
        else:
            for node in buffer:
                tordict[node[0]] += nodes + unreachable + ((node[1] / eq_path) if eq_nodes > 1 else 0)
            buffer = []
            nodes += eq_nodes
            eq_path = val[1]
            eq_nodes = 1
            prev = (val[0],val[2])
            if tordict.has_key(item):
                buffer = [(item,val[1])]
    # leftover nodes in buffer
    for node in buffer:
        tordict[node[0]] += nodes + unreachable + ((node[1] / eq_path) if eq_nodes > 1 else 0)


#start = time.time()

#counter = 99
for item in asdict:
    #print "item is %s =========" % item
    graph = init(item)
    bfs_pc([item])
    bfs_pp([item])
    bfs_cp(item)
    graph.pop(item,None)
    update_resilience()
    #print tordict
    #if counter <= 0:
    #    break
    #else:
    #    counter -= 1

#end = time.time()
#print end - start

#normalize the resiliency data to [0,1]
divid = (total_as - 2) * (total_as - 1)
for item in tordict:
    tordict[item] = tordict[item] / divid

with open('data.json', 'w+') as fp:
    json.dump(tordict, fp)




