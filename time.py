#!python
#coding:utf-8

import datetime
import time

print time.time()
print datetime.time.now()

basestr = '1970-1-1'
basetime = datetime.datetime.strptime(s,"%Y-%m-%d")

#时间字符串，从时间戳？
ltime=time.localtime(1237515355.0)
timeStr=time.strftime("%Y-%m-%d %H:%M:%S", ltime)


#时间字符串
now = datetime.datetime.now()  #这是时间数组格式
otherStyleTime = now.strftime("%Y-%m-%d %H:%M:%S")

# 时间加减操作，
now = datetime.datetime.now()
date = now + datetime.timedelta(days=-i)
str = date.strftime("%y_%m_%d")  # %Y是4位数如2017; %y是2位数，如17;
