import sys

# usage: python time.py <threshold value>

f = open('tor_log.txt', 'r')
time_map = {} # <(prefix,originAS) -> time announced>
bool_map = {} # <(prefix,originAS) -> '' or latest announcement time>
pref_map = {} # <pref -> latest_asn>
last_time = ''
total_time = {} # <pref -> total_announced_time>
for line in f:
    if line.split(" ")[5].strip() == 'A':
        pref = line.split(" ")[11][1:-2].strip()
        asn = line.split(" ")[13][1:-2].split(" ")[-1].strip()
        ts = line.split(" ")[3].strip() 
        if (not (pref,asn) in bool_map) or bool_map[(pref,asn)] == '':
            bool_map[(pref,asn)] = ts
            pref_map[pref] = asn
    else:
        pref = line.split(" ")[9][1:-3].strip()
        if pref in pref_map:
            asn = pref_map[pref]
            if ((pref,asn) in bool_map) and bool_map[(pref,asn)] != '':
                asn = pref_map[pref]
                ts = line.split(" ")[3].strip()
                new_ts = float(ts) - float(bool_map[(pref,asn)])
                if (pref,asn) in time_map:
                    time_map[(pref,asn)] += new_ts
                else:
                    time_map[(pref,asn)] = new_ts
                bool_map[(pref,asn)] = ''
    last_time = line.split(" ")[3].strip()

for b in bool_map:
    if bool_map[b] != '':
        if b in time_map:
            time_map[b] += (float(last_time) - float(bool_map[b]))
        else:
            time_map[b] = (float(last_time) - float(bool_map[b]))

total = 0
for t in time_map:
    pref = t[0]
    if pref in total_time:
        total_time[pref] += time_map[t]
    else:
        total_time[pref] = time_map[t]
    total += 1
print total

fp = 0
for x in time_map:
    pref = x[0]
    if (float(total_time[pref]) != float(0.0)) and (float(time_map[x]) != float(0.0)) and float(float(time_map[x])/float(total_time[pref])) < float(sys.argv[1]):
        fp += 1
        print x, time_map[x], float(float(time_map[x])/float(total_time[pref]))

print fp
