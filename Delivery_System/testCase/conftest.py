import pytest
from libs.login import Login
from configs.config import NAME_PSW
from libs.shop import Shop

#
# @pytest.fixture(autouse=True,scope='function')
# def start_running():
#     print("自动化项目开始执行-------")
#     yield
#     print("自动化项目结束执行-------，清除数据")
#--------------------------------登录-------
@pytest.fixture(scope='class')
def login_init():
    print("登录初始化操作开始--------")
    token = Login().login(NAME_PSW,getToken=True)
    yield token   #返回值将token返回
    print("登录初始化操作完成------")


#------------------店铺实例------------
#如果fixture需要使用另一个fixture的返回值，直接使用另一个的函数名即可
@pytest.fixture(scope='class')
def shop_init(login_init):
    print("创建店铺实例初始化操作开始---------")
    shopObject = Shop(login_init)
    yield shopObject
    print("创建店铺实例初始化操完成---------")

