# -*- coding:utf-8 -*-
#Author: homoo
#Data: 2020/3/16
#File: do_mysql.py

import pymysql

mysql_config={
    'host':'127.0.0.1',
    'user':'root',
    'password':'123456',
    'port':3306,
    'database':'plesson'
}

cnn=pymysql.connect(**mysql_config)

cursor = cnn.cursor()

query_sql="select * from sq_course"
query_sql="select Colume from sq_course.colume"

cursor.execute(query_sql)
a=cursor.fetchall()
print(a)
