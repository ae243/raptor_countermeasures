import sys
from netaddr import IPNetwork, IPAddress

f = open('ips.txt', 'r')
ips = []
for line in f:
    ips.append(line.strip())
f.close()

f = open('indosat_updates_april.txt', 'r')
prefs = []
for line in f:
    prefs.append(line.split("|")[6].strip())
f.close()

count = 1
f = open('tor_indosat_updates.txt', 'w')
for ip in ips:
    print str(count) + "/" + str(len(ips))
    found = False
    for p in prefs:
        if IPAddress(ip) in IPNetwork(p):
            found = True
            f.write(ip + "|" + p + "\n")
            break
    count += 1
f.close()
