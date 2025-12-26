# -*- coding: utf-8 -*-
# @File    : baseAPI.py
# @Time    : 2021/11/12 20:53
# @Author  : xintian
# @Email   : 1730588479@qq.com
# @Software: PyCharm
# Date:2021/11/12
print()
import requests
from utils.handle_path import config_path
from utils.handle_log import log
import traceback
"""
没有封装的接口代码：每一个自动化测试方法都需要加异常机制+log
基类的封装思路：
    1- 加入异常机制+log
    2- 截图操作---ui 自动化
    3- 一般模块的常用接口：
        增删改查 
    4- 代码不太可能一次性写的完整！
def request(method, url, **kwargs)
#
method, url
接口风格：
    1- 常规风格：
        1、一个模块，增删改查的4个接口的路径的不一样--自定义性比较强
        2、请求和响应数据类型不定
    2- restful风格
        1、一个模块，增删改查的4个接口的路径的一样的
        2、请求和响应数据类型一样的--json格式

一个项目的版本定下来之后：
    一个接口有10个用例：
        1- 变的是： 接口的描述、接口的用例请求参数、预期的响应
        2- 不变的是: url  请求方法
"""
from utils.handle_yml import get_yaml_data
import inspect
from configs.config import HOST
import os


"""
公共的基类关于token  公共鉴权值怎么处理：
    1- 登录接口不需要
    2- 其他业务接口一定

"""


class BaseApi:  # 基类
    def __init__(self, inToken=None,file=None):  # 初始化方法
        if inToken:  # 业务接口 传递了token---inToken=有值
            self.header = {'Authorization': inToken}
        else:  # 登录接口不需要token传入的
            self.header = None

        # __class__.__name__ 获取类名
        # print('当前类名是>>> ',self.__class__.__name__)
        # 通过模块名去获取对应模块的数据
        self.data = get_yaml_data(os.path.join(config_path,'apiPathConfig.yml'))[self.__class__.__name__]
        print("self.data",self.data)
    # --------公共的发送方法----------每一个接口方法都会调用这个去发送请求
    def request_send(self, data=None, json=None, param=None, file=None, id=''):
        try:
            methodName = inspect.stack()[1][3]  # 谁调用了我，他的函数名
            path, method = self.data[methodName].values()
            print("path, method:--->",path, method)
            # 数据---需要剥离对应某一个接口的数据
            resp = requests.request(method=method, url=f'{HOST}{path}' + str(id), data=data, json=json, params=param,
                                    files=file, headers=self.header)

            return resp.json()
        except Exception as error:
            # 打日志
            log.error(traceback.format_exc())

    # 1- 新增接口：
    def add(self, inData):
        return self.request_send(data=inData)

    # 2- 删除接口---对应某一个id  删除  /delete/api/{id}
    def delete(self):
        pass

    # 3- 更新接口
    def update(self, inData):
        return self.request_send(data=inData)

    # 4- 查询接口
    def query(self, inData):
        return self.request_send(param=inData)

    # 5- 文件上传
    """
    工作中遇到不怎么接触的接口的时候：
        1- 网上了解下接口的用法
        2- 抓包去观察--找到门路

    请求体数据   
    # 123.png
    userFile = {'变量名':(文件名，文件对象,文件类型)} 
    """

    def file_upload(self, fileDir: str):  # d:/123.png
        #  示例： d:/123.png
        # fileName =123.png    fileDir=d:/123.png   ,fileType=png
        fileName = fileDir.split('\\')[-1]
        fileType = fileDir.split('.')[-1]
        userFile = {'file': (fileName, open(fileDir, mode='rb'), fileType)}
        return self.request_send(file=userFile)


# ------------------------------------------------------
class ApiAssert:
    @classmethod  # 类方法
    def define_api_assert(cls, result, condition, exp_result):
        try:
            if condition == '=':
                assert result == exp_result
                a
            elif condition == 'in':
                assert exp_result in result
        except Exception as error:
            log.error(traceback.format_exc())
            raise error  # 抛出异常---不影响pytest 运行结果！



# ---------------------------扩展-------------
"""
inspect
 1- 可以获取类或函数的参数的信息
 2- 获取当前本函数的函数名
 3- 获取调用函数的函数名

"""
# import inspect,sys
# def a():
#     print('执行函数---a')
#     print('谁调用了我a，哪一个函数名>>> ',inspect.stack()[1][3])
#
# def b():
#     print('执行函数---b')
#     a()
#     #print('b函数---当前自己的函数名',sys._getframe().f_code.co_name)
#
# def c():
#     a()
#
#
#
# c()

#  allure -serve  -h 具体本机ip -p 端口 json文件路径
