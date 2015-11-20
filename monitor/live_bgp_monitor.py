import sys
import subprocess
import ipaddr
from _pybgpstream import BGPStream, BGPRecord, BGPElem

def check_pfx(pfx, pfx_list):
    for p in pfx_list:
        if ipaddr.IPv4Network(pfx.strip()).overlaps(ipaddr.IPv4Network(p.strip())):
            return True
    return False

def asn_match(pfx, asn, as_map):
    if as_map[pfx] == asn:
        return True
    else:
        return False

pfx_list = []
f = open(sys.argv[1], 'r')
for line in f:
    pfx_list.append(line.strip())
f.close()

f_netcat_query = open('netcat_query.txt', 'w')
f_netcat_query.write('begin\n')
f_netcat_query.write('verbose\n')
for p in pfx_list:
    f_netcat_query.write(p + '\n')
f_netcat_query.write('end\n')
f_netcat_query.close()

command = ('netcat whois.cymru.com 43 < netcat_query.txt | sort -n > netcat_lookup.txt')
r = subprocess.Popen(command, shell=True)
r.wait()

as_map = {}
f_as = open('netcat_lookup.txt', 'r')
first = True
for line in f_as:
    if first:
        first = False
    elif line.split("|")[0].strip().isdigit():
        asn = line.split("|")[0].strip()
        pref = line.split("|")[2].strip()
        for x in pfx_list:
            if ipaddr.IPv4Network(pref.strip()).overlaps(ipaddr.IPv4Network(x.strip())):
                if x in as_map:
                    as_map[x].append(asn)
                else:
                    as_map[x] = [asn]

for ip in as_map:
    as_map[ip] = list(set(as_map[ip]))

stream = BGPStream()
rec = BGPRecord()

stream.add_filter('collector', 'rrc00')
stream.add_interval_filter(1438415400,-1)
stream.set_live_mode()

f2 = open('log.txt', 'w')
f3 = open('tor_log.txt', 'w')
f4 = open('tor_mismatch_log.txt', 'w')

stream.start()

while(stream.get_next_record(rec)):
    if rec.status != "valid":
        print rec.project, rec.collector, rec.type, rec.time, rec.status
    else:
        elem = rec.get_next_elem()
        while(elem):
            pfx = elem.fields['prefix']
            f2.write(rec.project + ' ' + rec.collector + ' ' + rec.type + ' ' + rec.time + ' ' + rec.status + ' ' + elem.type + ' ' + elem.peer_address + ' ' + elem.peer_asn + ' ' + elem.fields + '\n')
            if pfx in pfx_list or check_pfx(pfx, pfx_list):
                f3.write(rec.project + ' ' + rec.collector + ' ' + rec.type + ' ' + rec.time + ' ' + rec.status + ' ' + elem.type + ' ' + elem.peer_address + ' ' + elem.peer_asn + ' ' + elem.fields + '\n')
                asn = pfx = str(elem.fields['as-path']).split(" ")[-1]
                if not asn_match(pfx, asn, as_map):
                    f4.write(rec.project + ' ' + rec.collector + ' ' + rec.type + ' ' + rec.time + ' ' + rec.status + ' ' + elem.type + ' ' + elem.peer_address + ' ' + elem.peer_asn + ' ' + elem.fields + '\n')
                print rec.project, rec.collector, rec.type, rec.time, rec.status,
                print elem.type, elem.peer_address, elem.peer_asn, elem.fields
                elem = rec.get_next_elem()
