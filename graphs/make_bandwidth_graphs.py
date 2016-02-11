import sys
import constants

def bandwidth_per_as_graph(as_bw_map):
    data_map = constants.resilience_vals
    data_map2 = as_bw_map
    data_map3 = {}
    for asn in data_map2:
        data_map3[data_map2[asn]] = data_map[asn]

    # to make graph of resiliency based on number of relays in an AS
    od = collections.OrderedDict(sorted(data_map3.items()))

    x = od.values()
    y = od.keys()
    plt.plot(x, y, '.', markersize=20)
    plt.xlabel('Resilience')
    plt.ylabel('Bandwidth per AS')
    plt.title('Resilience and Corresponding Bandwidth per AS')
    plt.show()

f = open('2016-01-01-00-00-00-consensus', 'r')
got_ip = False
got_bw = False
ip = ''
bw = ''
bw_map = {}
for line in f:
    if line.split(" ")[0] == 'r':
        #get ip
        ip = line.split(" ")[6].strip()
        got_ip = True
    elif line.split(" ")[0] == 'w':
        #get bandwidth
        if got_ip:
            bw = line.split(" ")[1].split("=")[1].strip()
            got_bw = True
    if got_ip and got_bw:
        bw_map[ip] = bw
f.close()

as_map = {}
f = open('asn.txt', 'r')
for line in f:
    ip = line.split("|")[1].strip()
    asn = line.split("|")[0].strip()
    if ip == 'N/A' or asn == 'N/A':
        continue
    else:
        as_map[ip] = asn

# <as, bandwidth>
as_bw_map = {}
for ip in as_map:
    if as_map[ip] in as_bw_map:
        as_bw_map[as_map[ip]] += int(bw_map[ip])
    else:
        as_bw_map[as_map[ip]] = int(bw_map[ip])

bandwidth_per_as_graph(as_bw_map)
