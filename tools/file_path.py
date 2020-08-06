# -*- coding:utf-8 -*-
#Author: homoo
#Data: 2020/2/25
#File: file_path.py

import os


pro_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
# 测试用例路径
test_case_path = os.path.join(pro_path,'test_case')
# 测试数据路径
test_data_path = os.path.join(pro_path, 'data', 'test_data.xlsx')
# 测试报告路径
test_report_path = os.path.join(pro_path, 'result', 'html_report', 'html_report.html')
# 配置文件路径
config_path = os.path.join(pro_path, 'config', 'test_case.config')
# 日志文件路径
logs_path = os.path.join(pro_path, 'result', 'logs')
# print(test_case_path)
# print(test_data_path)d
# print(logs_path)

