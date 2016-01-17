import sys

file_list = ['2015-03-27-09-00-00-consensus', '2015-03-27-10-00-00-consensus', '2015-03-27-11-00-00-consensus', '2015-03-27-12-00-00-consensus', '2015-03-27-13-00-00-consensus', '2015-03-27-14-00-00-consensus', '2015-03-27-15-00-00-consensus']

f_res = open('relays.txt', 'a')
ip_list = []
for fi in file_list:
    f = open(fi, 'r')
    for line in f:
        x = line.split(" ")
        if x[0] == 'r':
            # get IP address and add to file
            ip = x[6]
            ip_list.append(ip)
    f.close()

ip_set = list(set(ip_list))
for ip in ip_set:
    f_res.write(str(ip) + '\n')
f_res.close()