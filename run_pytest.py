# -*- coding:utf-8 -*-
#Author: homoo
#Data: 2020/8/5
#File: run_pytest.py

import pytest

if __name__ == '__main__':
    pytest.main(["test_case/test_login_pytest.py", "test_case/test_add_course_pytest.py", "--junitxml=result/allure_report/report.xml",
                 "--html=result/allure_report/report.html", "--alluredir=result/allure_report/"])
    # pytest -m smoke --reruns-delay 5 -s --junitxml=result/htlm_report/
# test_case/test_login.py --junitxml=result/allure_report/report.xml --html=result/allure_report/report.html --alluredir=result/allure_report