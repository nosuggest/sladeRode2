#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : Case01.py
@Author: sladesha
@Date  : 2019/9/8 23:22
@Desc  : 
'''


class Person(object):
    # 类也是一个对象，执行定义class的时候，也执行了以下两行的代码
    name = "sal"
    print("___Person___")
    def __init__(self):
        self.name = "slade"


if __name__ == '__main__':
    pass
    print(Person)
    p = Person()
    print(p.name)