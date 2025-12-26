import pytest
from utils.handle_excel import get_excel_data
import allure
from common.baseApi import BaseAssert

@pytest.mark.food  # 增加标签 mark
@allure.epic('订餐系统')
@allure.feature('食品模块')  # 测试类
class TestFoodManage(BaseAssert):
    # 1- 添加食品种类
    @allure.story('添加食品种类')  # 接口的名称
    @allure.title('添加食品种类用例')  # 用例的标题
    @pytest.mark.food_add_kind  # 添加食品种类标签
    @pytest.mark.parametrize('caseTitle,inData,respData', get_excel_data('食品管理', 'Addfoodkind','标题','请求参数','响应预期结果'))
    @allure.title("{caseTitle}")
    def test_add_food_kind(self,caseTitle,inData, respData,food_init):
        if inData['restaurant_id']=='3269':
            inData['restaurant_id']=food_init.list_food({"page":1,"limit":1})['data']['records'][0]['restaurant_id']
        res = food_init.add(inData)
        '''
        如果断言不是一个属性，需要多个组合判断？
        原理：assert   布尔表达式       多个条件使用and  or
        '''
        self.define_assert(res, respData)
    #2- 添加食品
    @allure.story('添加食品')  # 接口的名称
    @allure.title('添加食品用例')  # 用例的标题
    @pytest.mark.food_add  # 增加食品标签
    @pytest.mark.parametrize('caseTitle,inData,respData', get_excel_data('食品管理', 'Addfood','标题','请求参数','响应预期结果'))
    @allure.title("{caseTitle}")
    def test_add_food(self, caseTitle,inData, respData,food_init):#传入食品初始化条件
        res = food_init.add(inData)
        self.define_assert(res, respData)

   #3- 列出食品
    @allure.story("列出食品")# 接口的名称
    @allure.title("列出食品接口用例")# 用例的标题
    @pytest.mark.food_list# 列出食品标签
    @pytest.mark.parametrize('caseTitle,inData,respData', get_excel_data("食品管理",'listfood','标题','请求参数','响应预期结果'))
    @allure.title("{caseTitle}")
    def test_list_food(self,caseTitle, inData, respData,food_init):#食物的初始化条件
        res = food_init.query(inData)
        self.define_assert(res, respData)

    #4- 编辑食品
    @allure.story("编辑食品")# 接口的名称
    @allure.title("编辑食品接口用例")# 用例的标题
    @pytest.mark.food_update# 修改食品标签
    @pytest.mark.parametrize('caseTitle,inData,respData',get_excel_data("食品管理",'updatefood','标题','请求参数','响应预期结果'))
    @allure.title("{caseTitle}")
    def test_update_food(self,caseTitle,inData,respData,update_food_init,food_init):#食物的初始化条件和更新的初始化条件
        if inData['id']=='id':#判断excel的值去改成现有查询的值
            inData['id']=update_food_init[2]#更新食品id
        if inData['idMenu']=='3209':#更新菜单id
            inData['idMenu']=update_food_init[0]
        if inData['idShop']=='3269':#更新店铺id
            inData['idShop']=update_food_init[1]
        # print(inData)
        res=food_init.update(inData)
        self.define_assert(res, respData)

    #5- 删除食品
    @allure.story("删除食品")
    @allure.title("删除食品接口用例")
    @pytest.mark.food_delete#删除食品标签
    @pytest.mark.parametrize('caseTitle,inData,respData',get_excel_data("食品管理",'deletefood','标题','请求参数','响应预期结果'))
    @allure.title("{caseTitle}")
    def test_delete_food(self,caseTitle,inData,respData,food_init,update_food_init):#传入食品初始化条件
        id=update_food_init[2]
        if inData['id']=='id':
            inData['id']=id
        res=food_init.delete(inData)
        self.define_assert(res, respData)

if __name__ == '__main__':
    # 本地运行处理历史数据
    # 1- 生成报告所需的数据    --alluredir ../report/tmp
    pytest.main(['test_food_manage.py', '-s', '--alluredir', '../report/tmp'])  # -s 打印print信息
    # 4- 生成打开测试报告---自动打开报告的服务
    # 需要默认设置下浏览器
    # os.system('allure serve ../report/tmp')