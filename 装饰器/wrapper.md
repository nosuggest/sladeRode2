# 什么是装饰器？
装饰器本质上是一个函数，该函数用来处理其他函数，它可以让其他函数在不需要修改代码的前提下增加额外的功能，装饰器的返回值也是一个函数对象。

# 通常的作用？
插入日志、性能测试、事务处理、缓存、权限校验以及各自高重复性的工作

# 执行顺序：
```python
@a
@b
@c
def t():
    pass
```
等价于
```
a(b(c(f())))
```

# 常用的内置装饰器？
@staticmethod
@classmethod
#property

# 写一个带参数的装饰器
```python
def disti(level = "1"):
    def dec(func):
        def wrapper(*args,**kwargs):
            if level == "1":
                print(1)
            else:
                print(2)
            return func(*args,**kwargs)
        return wrapper
    return dec
```

# functools.wraps作用？
这样的闭包的写法会把被修饰的函数func的__name__覆盖掉（func.__name__），用functools.wraps可以避免

# 类装饰器通过什么实现？
`__call__`

在算法模型的计算过程中，通常有很多中间变量，把这些中间变量都记录下来，可以更好的debug，用类装饰器就很好
```python
class PRec(object):
    def __init__(self,func):
        self.func = func
        # global
        self.content = {}

    def __call__(self,*args,**kwargs):
        tmp = self.func(*args,**kwargs)
        self.content.update(tmp)
        return tmp

@PRec
def add(a,b):
    return {"sum":a+b}
```