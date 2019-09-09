#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/9 9:01 AM
# @Author  : Slade
# @File    : Case01.py
import gc

'''
常见的方法：
1.引用计数
2.标记-清除的回收机制(Ruby)
3.分代回收
'''


class A():
    def __init__(self):
        pass

    def __del__(self):
        pass


class B():
    def __init__(self):
        pass

    def __del__(self):
        pass


a = A()
b = B()
# a与b之间构成了循环调用
a._b = b
b._a = a

# 虽然删除了a和b，但是ab对象之间还有引用，所以引用计数方法失效
del a
del b

print(gc.collect())
print(gc.garbage)
