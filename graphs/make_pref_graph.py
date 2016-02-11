import sys
import subprocess
import matplotlib.pyplot as plt

'''
f = open('2016-01-01-00-00-00-consensus','r')
ips = []
for line in f:
    if line.split(" ")[0] == 'r':
        i = line.split(" ")[6].strip()
        ips.append(i)
f.close()

print len(ips)

# run ips through team cymru to get prefix
f_netcat_query = open('netcat_query.txt', 'w')
f_netcat_query.write('begin\n')
f_netcat_query.write('verbose\n')
for i in ips:
    f_netcat_query.write(i + '\n')
f_netcat_query.write('end\n')
f_netcat_query.close()

command = ('netcat whois.cymru.com 43 < netcat_query.txt | sort -n > netcat_lookup.txt')
r = subprocess.Popen(command, shell=True)
r.wait()
'''

prefs = []
f = open('netcat_lookup.txt', 'r')
for line in f:
    prefs.append(line.split("|")[2].strip())
f.close()

lengths = []
for p in prefs:
    length = p.split('/')[1]
    lengths.append(int(length))

# make histogram of lengths
n, bins, patches = plt.hist(lengths, 50, facecolor='green')
plt.xlabel('Prefix Length')
plt.ylabel('Frequency')
#plt.title('Histogram of Tor-related AS Resiliency')
plt.axis([8, 25, 0, 1500])
plt.show()
