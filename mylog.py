#!/usr/bin/env python
#-*- coding = utf-8 -*-

'''
create 2017.07.23
__author__ = "cannnon-liu"

create screen log info
create file   log info

'''

'''
logging模块本身定义
CRITICAL = 50
FATAL = CRITICAL
ERROR = 40
WARNING = 30
WARN = WARNING
INFO = 20
DEBUG = 10
NOTSET = 0
'''


import logging
import getpass
import sys
import time
import os

#自定义一个自己使用的log类
class MyLog(object):
    def __init__(self,filename,path = './log/',file_level=logging.WARNING,console_level = logging.INFO):
        user = getpass.getuser()    #获取登录的用户名
        self.logger = logging.getLogger(user)

        self.filename = filename
        self.path = path

        '''定义输出到控制台中的信息，使用StreamHandler'''
        self.console_logger = logging.StreamHandler()  #输出到控制台
        self.console_logger.setLevel(console_level)  #定义输出到控制台的信息级别
        # 定义输出格式：当前时间，日志级别，logger的名字，用户输出的消息,
        console_format = '%(asctime)s  %(levelname)s  %(name)s  %(message)s'
        self.console_formatter = logging.Formatter(console_format)   #一定要对字符串格式化
        self.console_logger.setFormatter(self.console_formatter)




        '''定义输出到log文件中的信息,使用FileHandler'''
        self.path = path  # 选择路径，默认为./log

        logFile = self.path+self.filename+'.log'
        self.save_file(self.path)
        self.file_logger = logging.FileHandler(logFile)
        # 定义输出格式：当前时间，日志级别，logger的名字，用户输出的消息
        file_format = '%(asctime)s  %(levelname)s  %(name)s  %(module)s %(message)s'
        self.file_formatter = logging.Formatter(file_format)
        self.file_logger.setFormatter(self.file_formatter)
        self.file_logger.setLevel(file_level)

        self.logger.addHandler(self.console_logger)
        self.logger.addHandler(self.file_logger)

    '''选择控制台和log日志的记录级别'''
    def level(self):
        pass


    '''定义5个级别的信息输出函数'''
    def debug(self,msg):
        self.logger.debug(msg)

    def info(self,msg):
        self.logger.info(msg)

    def warn(self,msg):
        self.logger.warning(msg)

    def error(self,msg):
        self.logger.error(msg)

    def critical(self,msg):
        self.logger.critical(msg)


    '''设置log文件夹'''
    def save_file(self,path):

        file = path
        if os.path.exists(file):
            pass
        else:
            os.makedirs(file)

if __name__ == '__main__':
    mylog = MyLog(filename='test')
    mylog.debug("debug log")
    mylog.info("info log")
    mylog.warn("warn log")
    mylog.error("error log")
    mylog.critical("ctrical log")
