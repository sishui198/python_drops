# !/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'bit4'
__github__ = 'https://github.com/bit4woo'

from BaseHTTPServer import BaseHTTPRequestHandler
from StringIO import StringIO
import requests
import urlparse

class HTTPRepeater(BaseHTTPRequestHandler):
    def __init__(self, request_text,url,proxy=None):#还是要求url算了
        self.rfile = StringIO(request_text)
        self.raw_requestline = self.rfile.readline()
        self.parse_request()

        self.proxy = proxy
        self.method = self.command
        #self.data = self.rfile.read(int(self.headers['content-length'])) #固定长度
        self.data = self.rfile.read() #变动长度，直到结束；适合数据包修改之后。
        self.headers["content-length"] = str(len(self.data))#更新content-length,数据包修改过后
        self.header = self.headers.dict
        if "cookie"  in self.headers.keys():
            self.cookie = self.headers["Cookie"]
        else:
            self.cookie = None

        if url:
            print urlparse.urlparse(url)
            TextPath ="{0}?{1}".format(urlparse.urlparse(url).path,urlparse.urlparse(url).query)
            if TextPath == self.path:
                self.url = url
            else:
                print "Error! url is different from the request text"

        elif "origin" in self.headers.keys():
            self.url = self.headers["origin"]
        elif "referer" in self.header.keys() and "host" in self.header.keys():
            if urlparse.urlparse(self.headers["referer"]).netloc == self.headers["host"]:
                scheme = urlparse.urlparse(self.headers["origin"]).scheme
                self.url = "{0}{1}{2}".format(scheme, self.headers["host"], self.path)
        else:
            print("please specify the url")

    def show(self):
        print self.method
        print self.header
        print self.cookie
        print self.data
    def repeat(self):
        DoMethod = getattr(requests.Session(),self.method.lower())
        #if self.method
        if self.url.startswith("https://") and self.proxy:
            verify = False
        else:
            verify = True
        respone = DoMethod(self.url,headers=self.header,cookies = self.cookie,data = self.data,proxies = self.proxy,verify=verify)
        print respone.text



request_text = '''POST /downloads?client=navclient-auto-ffox&appver=59.0&pver=2.2 HTTP/1.1
Host: shavar.services.mozilla.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:59.0) Gecko/20100101 Firefox/59.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate
Content-Length: 349
Content-Type: text/plain
Connection: close
Pragma: no-cache
Cache-Control: no-cache

allow-flashallow-digest256;a:1490633678
base-track-digest256;a:1512580265
block-flash-digest256;a:1496263270
block-flashsubdoc-digest256;a:1512160865
except-flash-digest256;a:1494877265
except-flashallow-digest256;a:1490633678
except-flashsubdoc-digest256;a:1517935265
mozplugin-block-digest256;a:1471849627
mozstd-trackwhite-digest256;a:1524157865
'''

if __name__ == "__main__":
    proxy = {"http":"http://127.0.0.1:8080","https":"https://127.0.0.1:8080"}
    request = HTTPRepeater(request_text,"https://shavar.services.mozilla.com/downloads?client=navclient-auto-ffox&appver=59.0&pver=2.2",proxy)
    #request.show()
    request.repeat()
