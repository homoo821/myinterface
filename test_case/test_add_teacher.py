# -*- coding:utf-8 -*-
#Author: homoo
#Data: 2020/8/3
#File: test_add_teacher.py

import unittest
from ddt import ddt,data
from tools.read_excel_2 import ReadExcel
from api_test.http_request import HttpRequest
from tools.get_data import GetData
from tools.user_log import *
import json

test_data = ReadExcel().read_excel('add_teacher')

@ddt
class TestHttp(unittest.TestCase):

    def setUp(self):
        UserLog().info('==========开始测试==========')

    @data(*test_data)
    def test_add_teacher(self, test_data):
        UserLog().info('/*开始->ID:{0},标题:{1}*/'.format(test_data['ID'],test_data['title']))
        r = HttpRequest().http_request(test_data['url'], eval(test_data["header"]), eval(test_data['data']), test_data['method'], getattr(GetData,'Cookie'))
        UserLog().info('/*结束->ID:{0},标题:{1}*/'.format(test_data['ID'],test_data['title']))
        if r.cookies:
            setattr(GetData, 'Cookie', r.cookies)
        ReadExcel().writ_back(test_data_path, test_data['sheet_name'], int(test_data['ID'])+1, 'res', str(r.json()))
        print(r.json())
        try:
            self.assertEqual(r.json()['retcode'], test_data['exp'])
            testresult = 'Pass'
        except Exception as e:
            testresult = 'Fail'
            print(e)
            raise e
        finally:
            ReadExcel().writ_back(test_data_path, test_data['sheet_name'], int(test_data['ID']) + 1, 'testresult', testresult)

    def tearDown(self):
        UserLog().info('==========测试结束==========')

if __name__ == '__main__':
    unittest.main()
