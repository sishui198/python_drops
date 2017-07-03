# !/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'bit4'
__github__ = 'https://github.com/bit4woo'


#场景：根据一个字符串调用一个函数，函数名是通过字符串构成的。

class auto():
    def __init__(self):
        pass
    def a(self):
        print "aaaaaa"
    def b(self):
        print "bbbbbb"


#方法一
auto = auto()
mycmd = "a"

if mycmd=="a":
    auto.a()
elif mycmd == "b":
    auto.b()

#方法二

eval("auto."+mycmd)()

#方法三  # 推荐这种方法
method_to_call = getattr(auto, mycmd)
result = method_to_call()

