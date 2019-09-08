#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : Case03.py
@Author: sladesha
@Date  : 2019/9/8 23:29
@Desc  : 
'''
# 定义一个类
class Test:
    pass
t = Test()
print(type(t))

# 动态创建一个类
# type("Test1",(),{})及元类
Test1 = type("Test1",(),{})
t1 = Test1()
print(type(t1))

# 创建一个带有属性num的类
Person = type("Person",(),{"num":0})
p = Person()
print(p.num)

# 创建一个带有方法的类

def printNum(self):
    print("num")

Test2 = type("Test2",(),{"printNum":printNum})# 元类
t2 = Test2()#类
t2.printNum()
# 总结一下，元类就是类的类，元类创建出来类