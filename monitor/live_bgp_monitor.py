import sys
import subprocess
import ipaddr
from _pybgpstream import BGPStream, BGPRecord, BGPElem
import time
import threading

def check_pfx(pfx, pfx_list):
    for p in pfx_list:
        try:
            if ipaddr.IPv4Network(pfx.strip()).overlaps(ipaddr.IPv4Network(p.strip())):
                return [True, p]
        except ipaddr.AddressValueError:
            try:
                if ipaddr.IPv6Network(pfx.strip()).overlaps(ipaddr.IPv4Network(p.strip())):
                    return [True, p]
            except ipaddr.AddressValueError:
                return [False, '']
    return [False, '']

def asn_match(pfx, asn, as_map):
    if pfx in as_map:
        if asn in as_map[pfx]:
            return True
        else:
            print pfx, as_map[pfx], asn
            return False
    else:
        print pfx + " is not in the map."
        return False

def get_pfx_as(file_name):
    global pfx_list
    global as_map

    p_list = []
    f = open(file_name, 'r')
    for line in f:
        p_list.append(line.strip())
    f.close()

    f_netcat_query = open('netcat_query.txt', 'w')
    f_netcat_query.write('begin\n')
    f_netcat_query.write('verbose\n')
    for p in p_list:
        f_netcat_query.write(p + '\n')
    f_netcat_query.write('end\n')
    f_netcat_query.close()

    command = ('netcat whois.cymru.com 43 < netcat_query.txt | sort -n > netcat_lookup.txt')
    r = subprocess.Popen(command, shell=True)
    r.wait()

    as_map_temp = {}
    f_as = open('netcat_lookup.txt', 'r')
    first = True
    for line in f_as:
        if first:
            first = False
        elif line.split("|")[0].strip().isdigit():
            asn = line.split("|")[0].strip()
            pref = line.split("|")[2].strip()
            for x in p_list:
                if ipaddr.IPv4Network(pref.strip()).overlaps(ipaddr.IPv4Network(x.strip())):
                    if x in as_map_temp:
                        as_map_temp[x].append(asn)
                    else:
                        as_map_temp[x] = [asn]

    for ip in as_map_temp:
        as_map_temp[ip] = list(set(as_map_temp[ip]))

    pfx_list = p_list
    as_map = as_map_temp

def help_update_prefixes():
    while True:
        time.sleep(3600)
        new_file = 'prefix.txt'
        get_pfx_as(new_file)

pfx_list = []
as_map = {}
get_pfx_as(sys.argv[1])

# start new thread to pull new file from Yixin's machine, and call get_pfx_as(new file) and repeat this every hour 
t = threading.Thread(target=help_update_prefixes)
t.start()

print "PFX LIST: \n"
print pfx_list

stream = BGPStream()
rec = BGPRecord()

current_unix_epoch = int(time.time())
stream.add_filter('project', 'routeviews')
stream.add_filter('project', 'ris')
stream.add_interval_filter(current_unix_epoch,-1)
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
            if elem.type == 'A' or elem.type == 'W':
                pfx = elem.fields['prefix']
                f2.write(str(rec.project) + ' ' + str(rec.collector) + ' ' + str(rec.type) + ' ' + str(rec.time) + ' ' + str(rec.status) + ' ' + str(elem.type) + ' ' + str(elem.peer_address) + ' ' + str(elem.peer_asn) + ' ' + str(elem.fields) + '\n')
                [b, p] = check_pfx(pfx, pfx_list)
                if pfx in pfx_list or b:
                    f3.write(str(rec.project) + ' ' + str(rec.collector) + ' ' + str(rec.type) + ' ' + str(rec.time) + ' ' + str(rec.status) + ' ' + str(elem.type) + ' ' + str(elem.peer_address) + ' ' + str(elem.peer_asn) + ' ' + str(elem.fields) + '\n')
                    if elem.type == 'A':
                        asn = str(elem.fields['as-path']).split(" ")[-1]
                        if not asn_match(p, asn, as_map):
                            f4.write(str(rec.project) + ' ' + str(rec.collector) + ' ' + str(rec.type) + ' ' + str(rec.time) + ' ' + str(rec.status) + ' ' + str(elem.type) + ' ' + str(elem.peer_address) + ' ' + str(elem.peer_asn) + ' ' + str(elem.fields) + '\n')
            elem = rec.get_next_elem()
