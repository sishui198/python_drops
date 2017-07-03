#python
#coding:utf-8

import datetime
import urllib

def callbackfunc(blocknum, blocksize, totalsize):
    pass
for i in range(1,200):
    now = datetime.datetime.now()
    date = now + datetime.timedelta(days=-i)
    str = date.strftime("%y_%m_%d") #%Y 2017; %y 17;
    url = "https://xxx.com/Application/Runtime/Logs/Admin/{0}.log".format(str)
    print url
    #urllib2.urlopen("https://xxx.xxx.com/Application/Runtime/Logs/User/17_06_21.log")
    response = urllib.urlretrieve(url,"D:\\admin\\"+str+'.log',callbackfunc)