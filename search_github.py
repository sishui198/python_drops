# !/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'bit4'
__github__ = 'https://github.com/bit4woo'
import httplib
import re
import time
import requests

class search_github:

    def __init__(self, word, limit, useragent, proxy=None):
        self.engine_name = "Github"
        self.word = word.replace(' ', '%20')
        self.results = ""
        self.totalresults = ""
        self.server = "github.com"
        self.limit = int(limit)/10
        self.counter = 1 #页码
        self.headers = {"User-Agent":useragent}
        self.proxies = proxy

    def do_search(self):
        try:
            #https://github.com/search?p=2&q=api.map.baidu.com%2Fhighacciploc%2Fv1&type=Code&utf8=%E2%9C%93
            url = "https://{0}/search?p={1}&q={2}&type=Code&utf8=%E2%9C%93".format(self.server,self.counter,self.word)# 这里的pn参数是条目数
            print url
        except Exception, e:
            print e
        try:
            r = requests.get(url, headers = self.headers, proxies = self.proxies,verify=False)
            self.results = r.content
            self.totalresults += self.results
        except Exception,e:
            print e

    def check_next(self):
        if "<a class=\"next_page\"" in self.results:
            return True
        else:
            return False

    def findkeys(self):
        links = re.compile(r"""&#8211;
      <a href=\"(.+?)\"""")
        return links.findall(self.totalresults)  # list

    def process(self):
        while (self.counter < self.limit):#and self.check_next()
            self.do_search()
            #self.do_search_vhost()
            time.sleep(1)
            self.counter += 1
            #print "\tSearching " + str(self.counter) + " results..."
    def run(self): # define this function,use for threading, define here or define in child-class both should be OK
        self.process()
        self.d = self.findkeys()
        return self.d


if __name__ == "__main__":
        print "[-] Searching in github:"
        useragent = "(Mozilla/5.0 (Windows; U; Windows NT 6.0;en-US; rv:1.9.2) Gecko/20100115 Firefox/3.6"
        keyword = raw_input("search what:")
        proxy = {"https": "https://127.0.0.1:8080"}
        search = search_github(keyword, 100, useragent,proxy)
        search.process()
        all_links = search.findkeys()
        print all_links