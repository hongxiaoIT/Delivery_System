"""
函数功能：
1- 获取请求的body与预期的响应结果！
2- 可以自定义获取对应的列数据
3- 需要获取测试用例的里面指定的用例运行！
具体方案：
用例筛选！
1- 全部执行 all
2- 分段执行 tc001-tc003 tc005-tc007
3- 随机执行某一个 tc001 tc004 tc008
4- 混合模式：['tc001','tc003-tc007','tc009']
框架层pytest只能定制化执行接口层--跑某一个接口，或者不跑某一个接口
但是:具体的测试用例的挑选，框架做不了!
"""
import xlrd#这个类主要用来处理读取excel里面的内容
import json
from utils.handle_yml import get_yaml_data
from utils.handle_path import config_path,data_path
import os
#--------------返回的数据判断是否是json数据，如果是普通字符串则不需要转化，如果是json数据则需要转化成普通字符串
def is_json(inStr):
    try:
        return json.loads(inStr)#是json格式转换成字典
    except:
        return inStr#不是json格式，则 将字符串原样返回



def get_excel_data(config_file,sheet_name,case_name,run_case=['all']):
    #获取yaml文件的获取
    config_data = get_yaml_data(os.path.join(config_path,config_file))
    #excel路径获取
    file_path = os.path.join(data_path,config_data['file_name'])
    args = config_data['col_name']
    print("args%s" % args)
    res_list = []
    #1、加载excel,formatting_info是用来保持Excel文件的样式
    work_book = xlrd.open_workbook(file_path,formatting_info=True)
    # workSheet = work_book.sheet_names()#所有的表名
    #2、获取对应sheet表名
    work_sheet = work_book.sheet_by_name(sheet_name)
    """
    函数调用者使用列名称，代码在读取数据的时候还是使用列编号，所以就需要将列名称和列编号进行转化
    """
    col_indexs = []#函数调用者输入列名称，转化后的列编号[4, 9, 11]
    for col_name in args:#遍历用户输入的列名称---colName是个元组
        col_indexs.append(work_sheet.row_values(0).index(col_name))

#---------------------挑选需要执行的测试用例--------
    run_case_data = []
    if 'all' in run_case:
        run_case_data = work_sheet.col_values(0)
    else:#1、某一个用例 2、某一段用例
        for one in run_case:
            if '-' in one:#表示说执行一段用例
                start , end = one .split('-')
                for i in range(int(start),int(end)+1):
                    run_case_data.append(case_name+f'{i:0>3}')#['Login001', 'Login002', 'Login003']
            else:
                run_case_data.append(case_name+f'{one:0>3}')#单个用例
    print("运行的用例--->",run_case_data)

    row_idx = 0#代表行号的初始值
    for one in work_sheet.col_values(0):
        if case_name in one and one in run_case_data:
            #条件满足，这一行数据的对应列是需要的数据
            col_datas = []#存放一行对应的很多列的数据
            for index in col_indexs:
                tmp = is_json(work_sheet.cell(row_idx,index).value)#读取某一个单元格数据
                col_datas.append(tmp)
            res_list.append(tuple(col_datas))
        row_idx += 1
    return res_list


if __name__ == '__main__':
    # res = get_excel_data('excelConfig.yml','登录模块','Login',run_case=['003-005','006'])
    res = get_excel_data('excelConfig.yml','我的商铺','listshopping',run_case=['001-007'])

    print(res)
    for one in res:
        print(one)

