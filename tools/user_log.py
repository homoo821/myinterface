# -*- coding:utf-8 -*-
#Author: homoo
#Data: 2020/2/26
#File: user_log.py

import logging
from tools.file_path import *

class UserLog():

    def user_log(self, msg, level='INFO'):
        # 日志收集器
        logger = logging.getLogger('homoo')
        # 设置级别
        logger.setLevel('DEBUG')
        # 设置输出格式
        formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息:%(message)s')
        # 输出渠道
        ch = logging.StreamHandler()
        ch.setFormatter(formatter)

        fh=logging.FileHandler(logs_path,encoding='utf-8')
        fh.setFormatter(formatter)
        # 指定输出渠道
        logger.addHandler(ch)
        logger.addHandler(fh)

        # 收集日志
        if level =='DEBUG':
            logger.debug(msg)
        elif level=='INFO':
            logger.info(msg)
        elif level=='WARNING':
            logger.warning(msg)
        elif level=='ERROR':
            logger.error(msg)
        elif level=='CRITICAL':
            logger.critical(msg)
        else:
            print('请核对你输入的日志级别！')

        # 关闭渠道
        logger.removeHandler(ch)
        logger.removeHandler(fh)

    def debug(self,msg):
        self.user_log(msg,'DEBUG')
    def info(self,msg):
        self.user_log(msg,'INFO')
    def warning(self,msg):
        self.user_log(msg,'WARNING')
    def error(self,msg):
        self.user_log(msg,'ERROR')
    def critical(self,msg):
        self.user_log(msg,'CRITICAL')
if __name__ == '__main__':
    UserLog().debug('asfe')