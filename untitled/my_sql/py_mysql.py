#-*-coding:utf-8-*-
#__author__ = 'zhengyj'


import pymysql
#建立连接
conn = pymysql.connect(host='192.168.95.11',port=3306,user='admin',password='makecook')
#建立游标
cursor = conn.cursor()
#操作数据库
cursor.execute('create table if not exists zyj.zyj (id INT not null,name CHAR(32) not null)')
cursor.execute('INSERT INTO zyj.zyj (id,name) VALUES (1,"ZHENGYJ"),(2,"XIECUI")')

cursor.execute("select * from zyj.zyj")
print(cursor.fetchall())
