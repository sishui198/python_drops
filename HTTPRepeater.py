# !/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'bit4'
__github__ = 'https://github.com/bit4woo'

from BaseHTTPServer import BaseHTTPRequestHandler
from StringIO import StringIO
import requests
import urlparse
from Cookie import SimpleCookie

class HTTPRepeater(BaseHTTPRequestHandler):
    def __init__(self,url, request_text,proxy=None):#还是要求url算了
        self.rfile = StringIO(request_text)
        self.raw_requestline = self.rfile.readline()
        self.parse_request()

        ###parameters that needed in repeater request
        self.proxy = proxy
        self.method = self.command
        #self.data = self.rfile.read(int(self.headers['content-length'])) #固定长度
        self.data = self.rfile.read() #变动长度，直到结束；适合数据包修改之后。
        self.header = self.headers.dict

        self.header["content-length"] = str(len(self.data))  # 更新content-length,数据包修改过后
        if "cookie"  in self.header.keys():
            cookie_string = self.header["cookie"]
            cookie = SimpleCookie(cookie_string)
            self.cookie = {i.key: i.value for i in cookie.values()}
            #self.cookie = Cookie.Cookie()
            #self.cookie.load(cookie_string)
        else:
            self.cookie = None


        #####do some check on url and request raw
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
        print("Method: {0}".format(self.method))
        print("Header: {0}".format(self.header))
        print("Cookie: {0}".format(self.cookie))
        print("Data: {0}".format(self.data))

    def repeat(self):#do request
        DoMethod = getattr(requests.Session(),self.method.lower())

        if self.url.startswith("https://") and self.proxy:
            verify = False
        else:
            verify = True
        respone = DoMethod(self.url,headers=self.header,cookies = self.cookie,data = self.data,proxies = self.proxy,verify=verify)
        return respone



request_text = '''GET /js/tabLib-min.js?v=20150120 HTTP/1.1
Host: start.firefoxchina.cn
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:59.0) Gecko/20100101 Firefox/59.0
Accept: */*
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate
Referer: http://start.firefoxchina.cn/
Cookie: Hm_lvt_dd4738b5fb302cb062ef19107df5d2e4=1523774432,1525787657,1525960159; uid=38oGHFrNZQkicW+AanPkAg==
Connection: close
'''

if __name__ == "__main__":
    proxy = {"http":"http://127.0.0.1:8080","https":"https://127.0.0.1:8080"}
    url = "http://start.firefoxchina.cn/js/tabLib-min.js?v=20150120"
    request = HTTPRepeater(url,request_text,proxy)
    request.show()
    request.repeat()
