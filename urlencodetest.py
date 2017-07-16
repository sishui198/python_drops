#python
#coding:utf-8

import urllib


url ='''https://fofa.so/result?q=app="OrientDB"&qbase64=YXBwJTIwIk9yaWVudERCIg==&page=22'''


xx  = '''app="OrientDB"'''
print urllib.quote(xx)
