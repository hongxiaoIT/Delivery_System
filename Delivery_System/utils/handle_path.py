import os
# print(__file__)#当前文件路径
# print(os.path.dirname(__file__))
#工程路径
project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#配置路径
config_path = os.path.join(project_path,'configs')
#data路径
data_path = os.path.join(project_path,'data')
#report路径
report_path = os.path.join(project_path,'report\\tmp')
#log路径
log_path = os.path.join(project_path,'logs')
