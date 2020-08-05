# # -*- coding:utf-8 -*-
# #Author: homoo
# #Data: 2020/2/29
# #File: test.py
#
# import requests
# import json
# header={"User-Agent":"Mozilla/5.0(Windows NT 6.1)"}
# url1 = 'http://120.78.128.25:8765/Frontend/Index/login'
# data1={"phone":"13825161923","password":"lemon123"}
# r1 = requests.post(url=url1,data=data1,headers=header)
# print(r1.text)
# print(r1.headers["Set-Cookie"])
#
# url = 'http://localhost/api/mgr/sq_mgr/'
# header={"User-Agent":"Mozilla/5.0(Windows NT 6.1)","Content-Type":"application/x-www-form-urlencoded",
# #         "Cookie":"Pycharm-df2c00ac=f0bfa5fa-bf37-4140-9195-bc4a322fc2a1; goSessionid=j5wML4oBLTKoE18Y9aOkEN6IOYNK0vPEkYIorE-MZz8%3D"}
# # header["Cookie"]=r1.headers["Set-Cookie"]
# # print(header)
# data={"action":"add_teacher","data":''}
# r = requests.post(url=url,data=data)
# print(r.status_code)


# str1 = {'data':'asfeia${name}dfgjw'}
# print(str1['data'].find("${name1}"))
# str1 = str1['data'].replace('${name}','')
# print(str1)
# lines=[]
# while True:
#     s = input()
#     if s:
#         lines.append(s.upper())
#     else:
#         break
# for e in lines:
#     print(e)

# import logging
#
# class UserLog():
#     def user_log(self):
#         logger = logging.getLogger("homoo")
#
#         logger.setLevel('INFO')
#         formatter = logging.Formatter('%(asctime)s->%(filename)s->%(message)s')
#         handler = logging.StreamHandler()
#         handler.setFormatter(formatter)
#         logger.addHandler(handler)
#
#         logger.info("sfe")
#         logger.info("sfe")
#
# UserLog().user_log()

# class TestData():
#
#     Cookie=None

import requests
header = {"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
          "Cookie":"Pycharm-df2c00ac=f0bfa5fa-bf37-4140-9195-bc4a322fc2a1; goSessionid=j5wML4oBLTKoE18Y9aOkEN6IOYNK0vPEkYIorE-MZz8%3D"}
url1 = 'http://localhost/api/mgr/sq_mgr/'
json = {"action":"add_teacher","data":{"username":"","courses":[{"id":26,"name":"语文"}],"realname":"teacher_1","desc":"老师1","display_idx":1,"password":"sq888"}}
r1 = requests.post(url=url1, json=json, headers=header)
print(r1.json())

# token = r1.json()["token"]

# url2 = 'http://121.41.14.39:9097/api/message'
# header2 = {"Content-Type": "application/json",
#           "X-AUTH-TOKEN": token}
# json1 = {"title": "xxx", "content": "bxd"}
# r2 = requests.post(url=url2, json=json1, headers=header2)
# print(r2.json())

# url3 = 'http://121.41.14.39:9097/api/messages/1/4'
# header2 = {"Content-Type": "application/json",
#           "X-AUTH-TOKEN": token}
# r3 = requests.get(url=url3, headers=header2)
# print(r3.json())