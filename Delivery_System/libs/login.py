import requests
import hashlib
import copy
from common.baseApi import BaseApi
from configs.config import NAME_PSW
from utils.casetime import show_time


#密码需要进行md5加密
def get_md5_data(pws:str):
    """
    :param pws:
    :return:
    """
    #实例化一个md5对象
    md5 = hashlib.md5()
    #调用加密方法
    md5.update(pws.encode('utf-8'))
    return md5.hexdigest()
    # __get_md5_data('hello')


class Login(BaseApi):
    @show_time
    def login(self,inData,getToken=False):
        inData = copy.copy(inData)#浅拷贝下数据--避免修改全局数据
        inData['password'] = get_md5_data(inData['password'])
        respData = self.request_send(data=inData)#发送请求
        if getToken: # 获取token
            return respData['data']['token']
        else:#获取响应数据
            return respData




if __name__ == '__main__':
    print(Login().login(NAME_PSW))

