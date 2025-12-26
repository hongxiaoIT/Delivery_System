import logging
import os
import datetime
from utils.handle_path import log_path

def logger(fileLog=True,name = __name__):
    #日志路径，路径+文件名+后缀
    logDir = F"{log_path}/{datetime.datetime.now().strftime('%Y%m%d%H%M')}.log"
    #创建日志对象
    logObject = logging.getLogger(name)
    #设置日志级别
    logObject.setLevel(logging.INFO)
    #设置日志内容
    fmt = '%(asctime)s - %(levelname)s - %(filename)s[%(lineno)d]: %(message)s'
    format = logging.Formatter(fmt)
    #是否打印到文件还是控制台
    if fileLog:
        #打印到文件
        handle = logging.FileHandler(logDir,encoding='utf-8')
        #日志内容和渠道绑定
        handle.setFormatter(format)
        #日志对象和渠道绑定
        logObject.addHandler(handle)
    else:
        # 打印到控制台
        handle2 = logging.StreamHandler()
        handle2.setFormatter(format)
        logObject.addHandler(handle2)
    return logObject

log = logger()

# if __name__ == '__main__':
#     logger(True)
