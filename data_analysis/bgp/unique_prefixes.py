import sys

f = open('tor_mismatch_log.txt', 'r')
prefs = []

for line in f:
    p = line.split(" ")[11][1:-2]
    prefs.append(p)

unique_prefs = list(set(prefs))
print unique_prefs
print len(unique_prefs)
