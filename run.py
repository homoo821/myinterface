# -*- coding:utf-8 -*-
#Author: homoo
#Data: 2020/2/24
#File: run.py

import unittest
from tools.HTMLTestReportEN import HTMLTestRunner
from test_case import test_http
# from test_case.test_http import TestHttp
from tools.file_path import *

suit = unittest.TestSuite()
loader = unittest.TestLoader()
suit.addTest(loader.loadTestsFromModule(test_http))
# suit.addTest(loader.loadTestsFromTestCase(TestHttp))
with open(test_report_path,'wb') as file:

    runner = HTMLTestRunner(stream=file,
                            verbosity=2,
                            title='auto_test_request',
                            description='this is the first html report',
                            tester='homoo')

    runner.run(suit)

