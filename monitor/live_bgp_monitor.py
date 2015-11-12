from _pybgpstream import BGPStream, BGPRecord, BGPElem

stream = BGPStream()
rec = BGPRecord()

stream.add_filter('collector', 'rrc11')
stream.add_interval_filter(0,0)
stream.set_live_mode()

stream.start()

while(stream.get_next_record(rec)):
    if rec.status != "valid":
        print rec.project, rec.collector, rec.type, rec.time, rec.status
    else:
        elem = rec.get_next_elem()
        while(elem):
            print rec.project, rec.collector, rec.type, rec.time, rec.status,
            print elem.type, elem.peer_address, elem.peer_asn, elem.fields
            elem = rec.get_next_elem()


