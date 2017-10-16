# !/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'bit4'
__github__ = 'https://github.com/bit4woo'

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('120.28.64.69', 8080))
s.send(r'GET http://www.ip.cn/getip.php?action=getip HTTP/1.1\r\nAccept: text/plain\r\n\r\n')
data1 = ''
while 1:
    data = s.recv(1024)
    print data
    if len(data) < 1024:
       break
s.close()