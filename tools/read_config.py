# -*- coding:utf-8 -*-
#Author: homoo
#Data: 2020/2/26
#File: read_config.py

import configparser
from tools.file_path import *

class ReadConfig():

    def read_config(self, file_name, section, option):
        cf = configparser.ConfigParser()
        cf.read(file_name)
        # 获取所有sections
        # cf.sections()
        # print(cf.items('modle'))
        return cf.get(section, option)

if __name__ == '__main__':
    cf = ReadConfig().read_config(config_path,'MODE','mode')
    print(type(cf))
    print(cf)