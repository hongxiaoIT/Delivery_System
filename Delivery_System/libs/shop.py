from symbol import return_stmt

from django.middleware.csrf import get_token

from libs.login import Login
from configs.config import NAME_PSW
from common.baseApi import BaseApi
from utils.handle_path import data_path

print()

"""
    1、列表接口
    2、编辑接口
    3、图片上传接口
"""


class Shop(BaseApi):
    #重写父类方法
    def update(self, inData,shopID,imageInfo):
        #更新店铺id
        inData['id'] = shopID
        inData['image_path'] = imageInfo
        inData['image'] = f'/file/getImgStream?fileName={imageInfo}'
        #调用父类的方法
        return super(Shop,self).update(inData)



if __name__ == '__main__':
    #1、登录操作-获取token
    token = Login().login(NAME_PSW,True)
    #2、查询商铺
    testData = {"page":1,"limit":20}
    res = Shop(token).query(testData)
    # print(res)
    #3、图片上传
    res1 = Shop(token).file_upload(data_path+r'\456.jpg')
    shopID = res1['data']['records'][0]['id']
    imageInfo = res1['data']['realFileName']
    testData1 = {}
    shop = Shop(token).update(testData1,shopID,imageInfo)
    print(shopID)
