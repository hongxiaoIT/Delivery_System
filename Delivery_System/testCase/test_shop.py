import sys

import pytest
from libs.login  import Login
from utils.handle_excel import get_excel_data
from utils.handle_path import report_path,data_path
from common.baseApi import ApiAssert
import allure
import os


@allure.epic('外卖系统')
@allure.feature('商铺模块')
@pytest.mark.shop#给这个类打上shop标签
# @pytest.mark.skip(reason='这个模块还未开发好，跳过执行')
# @pytest.mark.skipif(sys.platform != "win32",reason="条件满足就跳过")
class TestShop(ApiAssert):
    #登录方法
    @allure.story('商铺列表')
    @pytest.mark.parametrize('title,inBody,expData',get_excel_data('excelConfig.yml','我的商铺','listshopping'))
    @allure.title("{title}")  # 用例标题
    @pytest.mark.shop_list#给这个方法打上shop_list标签
    def test_shop_list(self,title,inBody,expData,shop_init):#shop_init初始化
        res = shop_init.query(inBody)
        self.define_api_assert(res['code'],'in',expData['code'])



    @allure.story('商铺编辑')
    @pytest.mark.shop_update#给这个方法打上shop_update标签
    @pytest.mark.parametrize('title,inBody,expData',get_excel_data('excelConfig.yml','我的商铺','updateshopping'))
    @allure.title("{title}")
    def test_shop_update(self,title,inBody,expData,shop_init):

        with allure.step('1、需要店铺实例'):
            pass
        with allure.step('2、获取shopId'):
            shopId = shop_init.query({"page": 1, "limit": 20})['data']['records']['0']['id']
        with allure.step('3、图片上传接口上传图片'):
            res1 = shop_init.file_upload(data_path + r'\456.jpg')
            imageInfo = res1['data']['realFileName']
        with allure.step('4、调用店铺编辑接口'):
            res2 = shop_init.update(inBody,shopId,imageInfo)
            self.define_api_assert(res2['code'],'in',expData['code'])



if __name__ == '__main__':
    #--clean-alluredir用来清除报告的历史数据
    pytest.main([__file__,'-s','-m','shop_list','--alluredir',report_path,'--clean-alluredir'])
    os.system(f'allure server{report_path}')