# !/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'bit4'
__github__ = 'https://github.com/bit4woo'

import requests
import json
from socket import inet_aton
from struct import unpack

# http://lbsyun.baidu.com/index.php?title=webapi/high-acc-ip


def ip2long(ip_addr):
    return unpack("!L", inet_aton(ip_addr))[0] #其实这里就进行了IP合法性检查，不合法的不能完成转换

def is_inner_ipaddress(ip):
    ip = ip2long(ip)
    return ip2long('127.0.0.0') >> 24 == ip >> 24 or \
            ip2long('10.0.0.0') >> 24 == ip >> 24 or \
            ip2long('172.16.0.0') >> 20 == ip >> 20 or \
            ip2long('192.168.0.0') >> 16 == ip >> 16

def checkIP(ip_addr):
    try:
        if is_inner_ipaddress(ip_addr):#是内网IP，不合法
            return 0
        else:
            return ip_addr
    except Exception,e:
        return 0

def where(ip_addr):
    url = 'http://api.map.baidu.com/highacciploc/v1?qcip={0}&qterm=pc&ak={1}&coord=bd09ll&extensions=3'.format(ip_addr,AK)
    r = requests.get(url)
    content = json.loads(r.content)
    return content
    #print content
    #print content['content']['formatted_address']

if __name__ == "__main__":
    ip = "1.0.0.1"
    ip = checkIP(ip)
    if ip==0:
        pass
    else:
        r = where(ip)
        try:
            print r['content']['location']
        except:
            print r['result']['error']
        finally:
            pass