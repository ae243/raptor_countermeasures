import sys

f = open('tor_log.txt', 'r')
session_map = {} # <(prefix, originAS) -> [sessions]> each session is collector+peer
for line in f:
    if line.split(" ")[5].strip() == 'A':
        pref = line.split(" ")[11][1:-2].strip()
        asn = line.split(" ")[13][1:-2].split(" ")[-1].strip()
        collector = line.split(" ")[2].strip()
        peer = line.split(" ")[6].strip() 
        session = collector + "_" + peer
        if (pref,asn) in session_map:
            session_map[(pref,asn)].append(session)
        else:
            session_map[(pref,asn)] = [session]

for s in session_map:
    print s, len(session_map[s])
