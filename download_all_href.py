#python
#coding:utf-8

#     decode              encode
#str ---------> unicode --------->str
#How to remember? D-->E

import urllib
import re
import os
import urlparse

def findLinks(htmlString):
    links = re.compile(r"target=\"_blank\" href =\"(.+?)\"")
    return links.findall(htmlString.decode("utf8")) #list


def download(url,domain,savedir=os.getcwd()):
    def callbackfunc(blocknum, blocksize, totalsize):
        pass
    if url.__contains__(domain):
        pass
    else:
        url = "http://"+domain+"/"+url
    print url
    #print urllib.urlencode(url.encode("utf8"))
    #url = "http://www.thegitc.com/ppt2017sh/AM01-%E4%BE%AF%E9%9C%87%E5%AE%87-%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD%E4%BA%91-AI%E6%97%B6%E4%BB%A3%E5%9F%BA%E7%9F%B3-1.pdf"
    #url = "http://www.thegitc.com/ppt2017sh/AM02-汤峥嵘-互联网教育的大发展和机遇-1.pdf"
    #url = u"http://www.thegitc.com/ppt2017sh/PM05-\u5f20\u4e91\u806a-\u767e\u5ea6\u7edf\u4e00\u5206\u5e03\u5f0f\u8ba1\u7b97\u6846\u67b6Bigflow.pdf" 上面拼接后的就是这
    print os.path.join(savedir,url.split('/')[-1])
    response = urllib.urlretrieve(url.encode("utf8"), os.path.join(savedir,url.split('/')[-1]), callbackfunc)

if __name__ == "__main__":
    url = raw_input("please input url:")
    url = url.replace(" ","")
    domain = urlparse.urlparse(url).netloc
    html = urllib.urlopen(url).read()
    #print html
    #print type(html)
    links = findLinks(html)
    print links
    for item in links:
        download(item,domain)