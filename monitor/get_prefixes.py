import threading
import time
import sys

def update_list():
    global pfx_list
    p_list = []
    while True:
        f = open(sys.argv[1], 'r')
        for line in f:
            p_list.append(line.strip())
        f.close()
        pfx_list = p_list
        p_list = []
        time.sleep(60)

pfx_list = []

t = threading.Thread(target=update_list)
t.start()

print pfx_list

print "****\n"

time.sleep(65)

print pfx_list
