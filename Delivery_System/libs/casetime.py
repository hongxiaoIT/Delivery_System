import time

#闭包的写法,在一个函数里面定义另外一个函数，内置函数使用的是外函数的一个变量，外函数的返回值是内置函数的函数对象
def show_time(func):
    def inner():
        start_time = time.time()
        func()
        end_time = time.time()
        print("测试用例执行的时间---：",end_time-start_time)
    return inner

@show_time#test_case = show_time(test_case)等价于这么写
def test_case():
    time.sleep(5)
    print("测试用例1执行-----")

@show_time
def test_case2():
    time.sleep(10)
    print("测试用例2执行----")


if __name__ == '__main__':
    test_case()
    test_case2()