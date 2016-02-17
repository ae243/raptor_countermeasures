import sys

# Analysis 1a: frequency that a source prefix is flagged as anomalous
def analysis1a():
    f = open('all_trace_anomalies.txt', 'r')
    freq_map = {}
    for line in f:
        ip = line.split("|")[1]
        if ip in freq_map:
            freq_map[ip] += 1
        else:
            freq_map[ip] = 1
    print "Num srcs: " + str(len(freq_map))

# Analysis 1b: frequency that a destination prefix is flagged as anomalous
def analysis1b():
    f = open('all_trace_anomalies.txt', 'r')
    freq_map = {}
    for line in f:
        ip = line.split("|")[2]
        if ip in freq_map:
            freq_map[ip] += 1
        else:
            freq_map[ip] = 1
    print "Num dests: " + str(len(freq_map))

# Analysis 1c: frequency that a (src,dest) pair is flagged as anomalous
def analysis1c():
    f = open('all_trace_anomalies.txt', 'r')
    freq_map = {}
    for line in f:
        ip = line.split("|")[1]
        ip2 = line.split("|")[2]
        if (ip,ip2) in freq_map:
            freq_map[(ip,ip2)] += 1
        else:
            freq_map[(ip,ip2)] = 1
    print "Num sets: " + str(len(freq_map))

# Analysis 1d: frequency of a specific path for a (src,dest) pair
def analysis1d():
    f = open('all_trace_anomalies.txt', 'r')
    path_map = {}
    for line in f:
        ip = line.split("|")[1]
        ip2 = line.split("|")[2]
        paths = line.split("|")[3:-1]
        if (ip,ip2) in path_map:
            path_map[(ip,ip2)].extend(paths)
        else:
            path_map[(ip,ip2)] = [paths]
    print "Num sets: " + str(len(path_map))

# Analysis2: does this prefix pair appear in anomalous BGP updates?
def analysis2():
    f = open('tor_mismatch_log.txt', 'r')
    for line in f:


# Analysis3: does this prefix pair have a different origin?
def analysis3():
    f = open('all_trace_anomalies.txt', 'r')
    count = 0
    diff_origin = 0
    for line in f:
        paths = line.split("|")[3:-1]
        origins = []
        for p in paths:
            origins.append(p.split(" ")[-1])
        if len(set(origins)) > 1:
            print paths
            diff_origin += 1
        count += 1
    print "Count: " + str(count)
    print "Diff origin: " + str(diff_origin)

# Analysis4: does this prefix pair have a different/new AS in the path? (And how many?)
def analysis4():
    print "implement me!"

#analysis3()

analysis1a()
analysis1b()
analysis1c()
analysis1d()
#f = open('all_trace_anomalies.txt', 'r')
#f.close()
