#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/9 1:16 PM
# @Author  : Slade
# @File    : case1.py

class Itcast(object):
    def __init__(self, sub1):
        self.sub1 = sub1
        self.sub2 = "cpp"

    def __getattribute__(self, item):
        if item == "sub1":
            print("log here")
            return "not allowed"
        else:
            return object.__getattribute__(self, item)


if __name__ == '__main__':
    it = Itcast("python")
    print(it.sub1)
    # log here
    # not allowed
    print(it.sub2)
    # cpp
