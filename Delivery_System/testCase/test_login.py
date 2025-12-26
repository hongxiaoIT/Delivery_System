import pytest
from libs.login  import Login
from utils.handle_excel import get_excel_data
from utils.handle_path import report_path,data_path
from utils.handle_yml import get_yamlCase_data
from common.baseApi import ApiAssert
import allure
import os

@allure.epic('外卖系统')
@allure.feature('登录模块')
@pytest.mark.login
class TestLogin(ApiAssert):
    #登录方法
    @allure.story('登录接口')
    # @pytest.mark.parametrize('title,req_body,exp_data',get_excel_data('excelConfig.yml','登录模块','Login'))
    @pytest.mark.parametrize('title,req_body,exp_data',get_yamlCase_data(data_path+'\\loginCase.yaml'))
    @allure.title("{title}")  # 用例标题
    def test_login(self,title,req_body,exp_data):
        #调用登录接口
        res = Login().login(req_body)
        #写断言判断是否符合预期
        assert res['msg'] == exp_data['msg']



if __name__ == '__main__':
    #--clean-alluredir用来清除报告的历史数据
    #需要接入到自动化集成项目里面
    pytest.main([__file__,'-s','--alluredir',report_path,'--clean-alluredir'])
    os.system(f'allure server{report_path}')