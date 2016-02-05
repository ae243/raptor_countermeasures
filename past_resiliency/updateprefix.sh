#!/bin/bash

#------------------------------------------
# Purpose: Update prefix.txt and convert to ASN
# Execution: sh updateprefix.sh
# Output: Update prefix.txt and asn.txt
#------------------------------------------

# Get IP addresses of all Tor relays
python get_ips.py 2016-01-01-00-00-00-consensus

# Process the prefix file for Team Cymru
sed '1s/^/begin\n/' ips.txt > tmp.txt
echo "end" >> tmp.txt

# Convert to ASN
netcat whois.cymru.com 43 < tmp.txt > asn.txt

# Get ASNs for all Tor relays
python get_asn.py
