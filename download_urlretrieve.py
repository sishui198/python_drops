#python
#coding:utf-8

# 下载url中的返回内容，保存成文件。

import urllib
import time


def callbackfunc(blocknum, blocksize, totalsize):
    pass

while True:
    ltime = time.localtime()
    timeStr=time.strftime("%Y-%m-%d-%H-%M-%S", ltime)
    response = urllib.urlretrieve('http://www.zhxhl.com/data/captcha/ckstr.php',"D:\\pic\\"+timeStr+'.jpg',callbackfunc)
