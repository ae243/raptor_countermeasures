import sys

f = open(sys.argv[1], 'r')
ips = []
for line in f:
    items = line.split(" ")
    if items[0] == 'r':
        #get ip address
        ips.append(items[6].strip())
f.close()

ips = list(set(ips))

f_out = open('ips.txt', 'w')
for ip in ips:
    f_out.write(ip + "\n")
f_out.close()
