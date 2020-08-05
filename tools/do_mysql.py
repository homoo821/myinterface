# -*- coding:utf-8 -*-
#Author: homoo
#Data: 2020/3/16
#File: do_mysql.py

import pymysql

mysql_config={
    'host':'47.107.168.87',
    'user':'python',
    'password':'python666',
    'port':3306,
    'database':'future'
}

cnn=pymysql.connect(**mysql_config)

cursor = cnn.cursor()

query_sql="select * from member"

cursor.execute(query_sql)
a=cursor.fetchall()
print(a)
