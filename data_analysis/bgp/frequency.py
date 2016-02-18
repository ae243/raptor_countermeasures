import sys

# usage: python frequency.py <threshold numerator>
# Calculates the frequency of an AS announcing a path to prefix p - if the frequency is below a threshold, then flag it.

f = open('tor_log.txt', 'r')
count_map = {} # <(prefix,originAS) -> count>
total_map = {} # <prefix -> number of total announcements>
for line in f:
    if line.split(" ")[5] == 'A':
        prefix = line.split(" ")[11][1:-2].strip()
        origin_as = line.split(" ")[13][1:-2].split(" ")[-1].strip()

        if (prefix,origin_as) in count_map:
            count_map[(prefix,origin_as)] += 1
        else:
            count_map[(prefix,origin_as)] = 1

        if prefix in total_map:
            total_map[prefix] += 1
        else:
            total_map[prefix] = 1

unique_asns = []
unique_prefs = []
freq_map = {}
fp = 0
for x in count_map:
    pref = x[0]
    total = total_map[pref]
    count = count_map[x]
    fraction = float(float(count)/float(total))
    freq_map[x] = fraction
#    if fraction < float(float(sys.argv[1])/float(total_map[pref])):
    if fraction < float(sys.argv[1]):
        fp += 1
        unique_prefs.append(x[0])
        unique_asns.append(x[1])
print fp
prefs = list(set(unique_prefs))
asns = list(set(unique_asns))
