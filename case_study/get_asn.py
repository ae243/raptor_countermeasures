import sys

f = open('hijacked_asn.txt', 'r')
asn_list = []
first = True
for line in f:
    if first:
        first = False
    elif line.split("|")[0].strip().isdigit():
        asn_list.append(line.split("|")[0])
f.close()

asn_list = list(set(asn_list))

f_out = open('hijacked_toras.txt', 'w')
for asn in asn_list:
    f_out.write(asn + "\n")
f_out.close()
