# !/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'bit4'
__github__ = 'https://github.com/bit4woo'

import requests

from gevent import monkey
monkey.patch_all()
from gevent.pool import Pool
import Queue

SuccessProxiesQueue = Queue.Queue()

HEADER = {
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
    'Accept-Encoding': 'gzip, deflate',
}

def parse_proxies(proxy_file = 'proxy_list.txt'):

    ProxiesList  = []
    with open(proxy_file,'r') as fp:
        for line in fp:
            proxy = line.replace("\n","")
            ProxiesList.append(proxy)

    return ProxiesList

def check_proxy(proxy_ip):
    try:
        proxy = {"http": "http://" + proxy_ip, "https": "https://" + proxy_ip}

        r = requests.get(url="http://65.61.137.117/images/logo.gif", headers=HEADER,
                         timeout=5, proxies=proxy)
        if r.status_code == 200:
            # print proxy_ip
            SuccessProxiesQueue.put(proxy_ip)

        return True
    except Exception,e:
        return False


def check_sockt_proxy(proxy_ip):
    print "[+] check "+proxy_ip
    host = proxy_ip.split(":")[0]
    port = proxy_ip.split(":")[1]
    try:
        import socket
        import socks
        import requests

        socks.set_default_proxy(socks.SOCKS5, host, int(port))
        socket.socket = socks.socksocket
        socket.timeout = 5
        print(requests.get("http://ifconfig.io/ip",timeout=3).content)
        print "[success]" + proxy_ip
        # socks.set_default_proxy()
    except Exception,e:
        print e
        return False

def run():

    worker_pool = Pool(20)
    proxy_list = parse_proxies("socket.txt")

    # worker_pool.map(check_proxy, proxy_list)

    worker_pool.map(check_sockt_proxy, proxy_list)

    while True:
        if not SuccessProxiesQueue.empty():
            print SuccessProxiesQueue.get()
        else:
            break


if __name__ == "__main__":
    run()