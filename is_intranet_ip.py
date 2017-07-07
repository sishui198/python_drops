# !/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'bit4'
__github__ = 'https://github.com/bit4woo'

# 参考phthion的文章
# https://www.leavesongs.com/PYTHON/defend-ssrf-vulnerable-in-python.html
from socket import inet_aton
from struct import unpack

def ip2long(ip_addr):
    return unpack("!L", inet_aton(ip_addr))[0]

def is_inner_ipaddress(ip):
    ip = ip2long(ip)
    return ip2long('127.0.0.0') >> 24 == ip >> 24 or \
            ip2long('10.0.0.0') >> 24 == ip >> 24 or \
            ip2long('172.16.0.0') >> 20 == ip >> 20 or \
            ip2long('192.168.0.0') >> 16 == ip >> 16