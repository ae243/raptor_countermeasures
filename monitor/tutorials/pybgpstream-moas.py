from _pybgpstream import BGPStream, BGPRecord, BGPElem
from collections import defaultdict

stream = BGPStream()
rec = BGPRecord()

stream.add_filter('collector', 'route-views.sg')
stream.add_filter('record-type', 'ribs')
stream.add_interval_filter(1438415400, 1438416600)

stream.start()

prefix_origin = defaultdict(set)

while(stream.get_next_record(rec)):
    elem = rec.get_next_elem()
    while(elem):
        # Get the prefix
            pfx = elem.fields['prefix']
            # Get the list of ASes in the AS path
            ases = elem.fields['as-path'].split(" ")
            if len(ases) > 0:
                # Get the origin AS
                origin = ases[-1]
                # Insert the origin ASn in the set of origins for the prefix
                prefix_origin[pfx].add(origin)
            elem = rec.get_next_elem()

# Print the list of MOAS prefix and their origin ASns
for pfx in prefix_origin:
    if len(prefix_origin[pfx]) > 1:
        print pfx, ",".join(prefix_origin[pfx])
