import sys

f = open('tor_indosat_updates.txt', 'r')
ips = []
for line in f:
    ips.append(line.split("|")[0].strip())
f.close()

ips_set = list(set(ips))

f = open('hijacked_ips.txt', 'w')
for ip in ips_set:
    f.write(ip + '\n')
f.close()
