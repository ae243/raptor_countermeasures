import sys
import os

# for every file in log_012520_020921 directory:
#   1) remove NA
#   2) remove any duplicates - we only care about the set of ASes on the path
#   3) compare sets of ASes on paths -> if they are the same, then remove them, otherwise leave them
#   4) Analysis1: does this prefix pair see this really often (what percentage of days/hours)?
#   5) Analysis2: does this prefix pair appear in anomalous BGP updates?
#   6) Analysis3: does this prefix pair have a different origin?
#   7) Analysis4: does this prefix pair have a different/new AS in the path?  (we don't care about duplicates because we only care about the set of ASes that are on the path)

f_res = open('all_trace_anomalies.txt', 'w')
count = 1
for filename in os.listdir('../log_012520_020921'):
    print "Processing " + str(count) + "/" + str(len(os.listdir('../log_012520_020921')))
    f = open('../log_012520_020921/' + filename, 'r')
    for line in f:
        paths = line.split("|")[2:]
        sets = []
        for p in paths:
            as_set = sorted(list(set(p.split(" "))))
            #print sorted(list(set(p.split(" "))))
            #print as_set
            if 'NA' in as_set:
                as_set.remove('NA')
            clean_as_set = []
            for asn in as_set:
                clean_as_set.append(asn.strip())
            sets.append(' '.join(clean_as_set))
        if len(list(set(sets))) > 1:
            set_string = ''
            for s in sets:
                set_string += s
                set_string += "|"
            f_res.write(filename + "|" + line.split("|")[0] + "|" + line.split("|")[1] + "|" + set_string + "\n")
    f.close()
    count += 1
f_res.close()

# Analysis1: does this prefix pair see this really often (what percentage of days/hours)? (Does it always see the same differing sets of ASes?) (How many times in an hour does it see a different set?) 

# Analysis2: does this prefix pair appear in anomalous BGP updates?

# Analysis3: does this prefix pair have a different origin?

# Analysis4: does this prefix pair have a different/new AS in the path? (And how many?)
