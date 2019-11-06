# __init__方法
- __init__方法负责对象的初始化
    - 对象哪里来的呢？__new__ 方法的返回值就是类的实例对象
- 类似Java中的构造函数

# 利用__new__实现单例模式
 ```
class test(object):
    _single = None
    def __new__(cls,*a,**k):
        if not cls._single:
            # cls._single = object.__new__(cls,*a,*k)
            cls._single = random.random()
        return cls._single

class r(test):
    """docstring for r"""
    def __init__(self):
        print(self._single)
r1 = r()
r2 = r()
r1==r2
 ```
 
 # 解释一下__call__作用
 使得实例对象也将成为一个可调用对象，最常引用于类修饰器中