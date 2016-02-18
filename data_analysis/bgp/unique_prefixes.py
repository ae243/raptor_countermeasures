import sys

f = open('tor_log.txt', 'r')
prefs = []

for line in f:
    if line.split(" ")[5].strip() == 'A':
        p = line.split(" ")[11][1:-2]
        prefs.append(p)

unique_prefs = list(set(prefs))
print unique_prefs
print len(unique_prefs)
