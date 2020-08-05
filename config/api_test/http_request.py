# # -*- coding:utf-8 -*-
# #Author: homoo
# #Data: 2020/2/24
# #File: httptest.py

import requests
from tools.get_data import GetData

class HttpRequest():

    def http_request(self, url, header, data, method, cookies):
        if method == "get":
            r = requests.get(url=url, headers=header, data=data, cookies=cookies)
        elif method == 'post':
            r = requests.post(url=url, headers=header, data=data, cookies=cookies)
        else:
            print('暂不支持该种请求{}'.format(method))
        return r

if __name__ == '__main__':

    url='http://localhost/api/mgr/loginReq'
    # header={"Content-Type":"application/x-www-form-urlencoded"}
    data={"username":"auto","password":"sdfsdfsdf"}
    r=HttpRequest().http_request(url=url, header=None, data=data, method='post', cookies=None)
    print(r.json())