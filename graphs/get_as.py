import sys

f = open('2016-01-01-00-00-00-consensus', 'r')
ips = []
for line in f:
    if line.split(" ")[0].strip() == 'r':
        ip = line.split(" ")[6].strip()
f.close()

ips = list(set(ips))

f = open('asn.txt', 'r')
asn_map = {}
for line in f:
    asn = line.split("|")[0].strip()
    ip = line.split("|")[1].strip()
    if asn in asn_map:
        asn_map[asn] += 1
    else:
        asn_map[asn] = 1

