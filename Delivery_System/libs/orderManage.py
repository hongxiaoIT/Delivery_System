from libs.login import Login
from common.baseApi import BaseApi

class Order_admin(BaseApi):#订单管理
    pass

if __name__ == '__main__':
    getToken = Login().login({"username": "ka0181", "password": "26205"}, getToken=True)
    res = Order_admin(getToken).query({"page": "", "limit": 1})
    print(res)