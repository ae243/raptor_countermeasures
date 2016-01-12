import sys
import subprocess
import ipaddr
from _pybgpstream import BGPStream, BGPRecord, BGPElem
import time
import threading

def ip_in_pfx(ip_list, pfx):
    for ip in ip_list:
        try:
            pref = ipaddr.IPv4Network(pfx)
            if ip in pref:
                return True
        except:
            pref = ipaddr.IPv6Network(pfx)
            if ip in pref:
                return True
    return False

print "Starting script..."

ip_list = []
f_pfx = open('relays.txt', 'r')
for line in f_pfx:
    try:
        ip = ipaddr.IPv4Address(line.strip())
    except ipaddr.AddressValueError:
        ip = ipaddr.IPv6Address(line.strip())
    ip_list.append(ip)
f_pfx.close()

print "Got all relays' IP addresses..."

stream = BGPStream()
rec = BGPRecord()

start_unix_epoch = 1427452680
end_unix_epoch = 1427466360
stream.add_filter('project', 'routeviews')
stream.add_filter('project', 'ris')
stream.add_interval_filter(start_unix_epoch,end_unix_epoch)

print "Set stream filters..."

stream.start()

print "Started stream..."

f2 = open('log.txt', 'w')

while(stream.get_next_record(rec)):
    if rec.status != "valid":
        print rec.project, rec.collector, rec.type, rec.time, rec.status
    else:
        elem = rec.get_next_elem()
        while(elem):
            if elem.type == 'A':
                pfx = elem.fields['prefix']
                if (ip_in_pfx(ip_list, pfx)) and ("40633 18978" in str(elem.fields['as-path'])):
                    f2.write(str(rec.project) + ' ' + str(rec.collector) + ' ' + str(rec.type) + ' ' + str(rec.time) + ' ' + str(rec.status) + ' ' + str(elem.type) + ' ' + str(elem.peer_address) + ' ' + str(elem.peer_asn) + ' ' + str(elem.fields) + '\n')
            elem = rec.get_next_elem()
