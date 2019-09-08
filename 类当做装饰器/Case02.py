#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : Case02.py
@Author: sladesha
@Date  : 2019/9/8 23:07
@Desc  : 
'''


class Case:
    def __init__(self,func):
        print("func name is %s"%func.__name__)
        self.__func = func
    def __call__(self):
        print("开始装饰")
        # 意味着被装饰的函数带入此处，执行Case()的时候，相当于执行被装饰的函数+其他修饰的内容
        self.__func()
# @类，这样相当于创建了对应类的对象，创建对象类的时候，把testCase传进去了；等同于test=Test(test)
# 在上面这个case类中，case作为一个函数被传入了Case这个类中，作为一个参数；__call__自动调用这个类的function
@Case
def case():
    print("---------test------------")

if __name__ == '__main__':
    case()
    case()