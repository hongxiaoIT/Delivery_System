#安装环境yaml库
import os.path

import yaml
from utils.handle_path import config_path,data_path

def get_yaml_data(fileDir):
    with open(fileDir,encoding='utf-8') as fo:
        return yaml.safe_load(fo.read())#使用yaml库读取文件，转成字典

def set_yaml_data(inData,fileDir):
    with open(fileDir,'a',encoding='utf-8') as fo:
        return yaml.safe_dump(inData,fo)


def set_yamls_data(inData,fileDir):
    with open(fileDir,'w',encoding='utf-8') as fo:
        return yaml.safe_dump_all(inData,fo)


def get_yamlCase_data(fileDir):
    with open(fileDir,'r',encoding='utf-8') as fo:
        res = yaml.safe_load(fo.read())
        result_list = []
        for one in res:
            result_list.append((one['detail'],one['data'],one['resp']))
    return result_list

if __name__ == '__main__':
    # res = get_yaml_data(os.path.join(config_path,'apiPathConfig.yml'))
    # res = get_yaml_data(os.path.join(data_path,'data.yml'))
    # res = set_yaml_data({'name':'xiaohong'},"../data/xh.yaml")
    # testData =[[10,20,30],{'name':'xiaohong'}]
    # res = set_yamls_data(testData,'../data/xh1.yml')
    res = get_yamlCase_data('../data/loginCase.yaml')
    print(res)


#{'file_name': 'Delivery_System_V1.5.xls', 'col_name': ['标题', '请求参数', '响应预期结果']}
