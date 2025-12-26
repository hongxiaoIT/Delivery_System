#-*- coding: utf-8 -*-
#@File    : 装饰器操作.py
#@Time    : 2021/9/22 20:45
#@Author  : xintian
#@Email   : 1730588479@qq.com
#@Software: PyCharm
#Date:2021/9/22
print()
"""
自动化测试组：
    目前进度：
        1- 实现了登录、店铺自动化测试
    需求：
        是否可以打印下每一个测试用例执行的时间！
"""

#----------------------a  小明： 8000 ------
"""
方案描述：
    1- 直接在test_xxx里面加 计时操作
        startTime = time.time()
    讨论的结果：
        1- 代码修改量太大，而且改变了代码原有的结构
深挖需求：
    1- 尽可能不修改代码
    2- 不修改代码的结构
"""

#------------------方案二：小青  12000
#经过搜索--python有一个叫装饰器
#什么是装饰器？
#怎么使用装饰器？
"""
装包：在函数定义的时候  def test(*args,**kwargs)
    test(1,2,3,name=tom)---*args----装包成元组，**kwargs---装包成字典
解包：在函数调用的时候
     test(*[10,20])==test(10,20)
闭包：在一个函数里定义一个函数，内置函数使用了外函数的一个变量，外函数的返回值是内函数的函数对象

装饰器：在已有函数的功能上，不修改代码去扩展函数功能！
"""
import time
def show_time(func):
    def inner(*args):
        startTime = time.time()
        res = func(*args)#自动化测试用例执行过程---test_case()
        endTime = time.time()
        print('执行时间>>> ',endTime-startTime)
        print('hello')
        return res
    return inner


@show_time#等价于   test_case01 = show_time(test_case01) 等价于 test_case01 = inner
def test_case01():
    time.sleep(1)#模拟用例执行时间！
    print('---自动化测试用例执行01---')

@show_time
def test_case02():
    time.sleep(1)#模拟用例执行时间！
    print('---自动化测试用例执行02---')




if __name__ == '__main__':
    test_case01()#inner()
    test_case02()#inner()

