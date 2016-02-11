#!/bin/bash

#------------------------------------------
# Purpose: Update prefix.txt and convert to ASN
# Execution: sh updateprefix.sh
# Output: Update prefix.txt and asn.txt
#------------------------------------------

# Process the prefix file for Team Cymru
sed '1s/^/begin\n/' hijacked_ips.txt > hijacked_tmp.txt
echo "end" >> hijacked_tmp.txt

# Convert to ASN
netcat whois.cymru.com 43 < hijacked_tmp.txt > hijacked_asn.txt

# Get ASNs for all Tor relays
python get_asn.py
