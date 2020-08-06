# -*- coding:utf-8 -*-
#Author: homoo
#Data: 2020/8/5
#File: conftest.py

import pytest
from tools.user_log import UserLogs


@pytest.fixture()
def status_fixture():
    # 前置操作
    UserLogs().info("=====测试类执行之前执行=====")
    yield ()   # 分割线：返回值
    # 后置操作
    UserLogs().info("==========测试类执行之后执行==========")
