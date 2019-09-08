#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : Case02.py
@Author: sladesha
@Date  : 2019/9/8 23:26
@Desc  : 
'''

# 类对象创建
def choose(name):
    if name == "foo":
        class Foo:
            pass

        return Foo
    else:
        class Bar:
            pass

        return Bar

if __name__ == '__main__':
    choose("foo")