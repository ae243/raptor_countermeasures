import sys
import numpy
import matplotlib.pyplot as plt
import collections
import constants

# usage: python make_graphs.py

def plot_data(data, color):
    n, bins, patches = plt.hist(data, 50, facecolor='green', alpha=0.75)
    plt.xlabel('Resilience')
    plt.ylabel('# of ASes')
    plt.title('Histogram of Tor-related AS Resiliency')
    plt.axis([0, 1, 0, 35])
    plt.show()

data_map = constants.resilience_vals # as -> resilience

f = open('asn.txt', 'r')
asn_map = {}
for line in f:
    asn = line.split("|")[0].strip()
    ip = line.split("|")[1].strip()
    if asn != 'NA':
        if asn in asn_map:
            asn_map[asn] += 1
        else:
            asn_map[asn] = 1
f.close()

data_map2 =  asn_map # as -> num relays

od1 = collections.OrderedDict(sorted(data_map.items()))
od2 = collections.OrderedDict(sorted(data_map2.items()))

for o in od2:
    if int(od2[o]) > 100:
        print o, od2[o], od1[o]

data_map3 = {}
for asn in data_map2:
    data_map3[data_map2[asn]] = data_map[asn]

# to make graph of resiliency based on number of relays in an AS
od = collections.OrderedDict(sorted(data_map3.items()))

#for o in od:
#    print o, od[o]

print len(od1)
print len(od2)

x = od1.values()
y = od2.values()
plt.plot(x, y, '.', markersize=10)
plt.xlabel('Resilience')
plt.ylabel('# of Relays in AS')
plt.title('Resilience and Corresponding Number of Relays per AS')
plt.show()

# To plot histogram of resiliency
#data_list = data_map.values()
#plot_data(data_list, 'blue')
