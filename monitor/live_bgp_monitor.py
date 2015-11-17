import sys
from _pybgpstream import BGPStream, BGPRecord, BGPElem

pfx_list = []
f = open(sys.argv[1], 'r')
for line in f:
    pfx_list.append(line.strip())

stream = BGPStream()
rec = BGPRecord()

stream.add_filter('collector', 'rrc00')
stream.add_interval_filter(1438415400,-1)
stream.set_live_mode()

stream.start()

while(stream.get_next_record(rec)):
    if rec.status != "valid":
        print rec.project, rec.collector, rec.type, rec.time, rec.status
    else:
        elem = rec.get_next_elem()
        while(elem):
            pfx = elem.fields['prefix']
            if pfx in pfx_list:
                print rec.project, rec.collector, rec.type, rec.time, rec.status,
                print elem.type, elem.peer_address, elem.peer_asn, elem.fields
                elem = rec.get_next_elem()


