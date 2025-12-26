import pytest,os
from utils.handle_excel import get_excel_data
import allure
from common.baseApi import BaseAssert

@pytest.mark.order#订单标签
@allure.epic('订餐系统')
@allure.feature('订单模块')#测试类
class Testorder(BaseAssert):
    #1- 搜索订单
    @allure.story('订单搜索')#接口的名称
    @allure.title('订单搜索用例')  # 用例的标题
    @pytest.mark.order_search# 搜索订单标签
    @pytest.mark.parametrize('caseTitle,inData,respData',get_excel_data('我的订单','searchorder','标题','请求参数','响应预期结果'))
    @allure.title("{caseTitle}")
    def test_search_order(self,caseTitle,inData,respData,order_init):
        #1- 调用店铺列出接口
        #店铺实例的创建必须要登录--需要一个店铺的实例---才能使用对应的方法
        #调用对应的方法
        res = order_init.query(inData)
        self.define_assert(res, respData)
if __name__ == '__main__':
    #1- 生成报告所需的数据    --alluredir ../report/tmp
    pytest.main(['test_order_manage.py','-s','--alluredir','../report/tmp'])# -s 打印print信息
    #4- 生成打开测试报告---自动打开报告的服务
    #需要默认设置下浏览器
    #os.system('allure serve ../report/tmp')