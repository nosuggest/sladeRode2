#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : Case01.py
@Author: sladesha
@Date  : 2019/9/8 23:05
@Desc  : 
'''


class Test(object):
    def __call__(self, *args, **kwargs):
        print("this is Test")

if __name__ == '__main__':
    t = Test()
    # t直接调用，相当于调用__call__方法
    t()