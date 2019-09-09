#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/9 1:37 PM
# @Author  : Slade
# @File    : case4.py
class Person(object):
    def __getattribute__(self, item):
        if item.startswith("a"):
            return "haha"
        else:
            return object.__getattribute__(self, "test")  # 扔给父类处理

    def test(self):
        print("heihei")


if __name__ == '__main__':
    p = Person()
    print(p.a)
    # haha

    print(p.b)
    # 死循环，调用b属性的时候，进入test调用，test调用的时候又进入了__getattribute__，进入之后又进入了return self.test
