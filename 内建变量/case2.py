#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/9 1:22 PM
# @Author  : Slade
# @File    : case2.py
class Itcast(object):
    def __init__(self, sub1):
        self.sub1 = sub1
        self.sub2 = "cpp"

    def __getattribute__(self, item):
        print("=======>%s" % item)
        if item == "sub1":
            print("log here")
            return "not allowed"
        else:
            temp = object.__getattribute__(self, item)
            print("====>%s" % str(temp))
            return temp

    def show(self):
        print("here")


if __name__ == '__main__':
    it = Itcast("python")
    print(it.sub1)
    # =======>sub1
    # log here
    # not allowed

    print(it.sub2)
    # =======>sub2
    # ====>cpp
    # cpp

    it.show()
    # 相当于把show给了__getattribute__中的item，show的结果应该是一个方法。这就是方法的被调用的含义。
    # =======>show
    # 这边就是show的方法，这边show的方法也就是一个变量，只是可被调用的方法变量
    # ====><bound method Itcast.show of <__main__.Itcast object at 0x109e5d2b0>>
    # here
