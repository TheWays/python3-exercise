#!/usr/bin/env python3
# -*- coding: utf-8 -*-

########## prepare ##########

# install mysql-connector-python:
# pip3 install mysql-connector-python --allow-external mysql-connector-python

import mysql.connector

try:
    # change root password to yours:
    conn = mysql.connector.connect(user='', password='', database='practise')
    
    cursor = conn.cursor()
    # 创建user表:
    cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
    # 插入一行记录，注意MySQL的占位符是%s:
    cursor.execute('insert into user (id, name) values (%s, %s)', ('1', 'Michael'))
    print('rowcount =', cursor.rowcount)
    # 提交事务:
    conn.commit()
    cursor.close()

except Exception as e: 
    print('except:', e)
   
# 运行查询:
cursor = conn.cursor()
cursor.execute('select id, name from user')
values = cursor.fetchall()
for item in values:
        print("id:" + str(item[0]) + ",name:" + str(item[1]))
#print(values)
# 关闭Cursor和Connection:
cursor.close()
conn.close()
