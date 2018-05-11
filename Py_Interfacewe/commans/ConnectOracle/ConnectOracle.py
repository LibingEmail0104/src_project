#uncoding=utf-8
import cx_Oracle as oracle
import cx_Oracle
import unittest
import sys

print(sys.path)
print("cx_Oracle.version:", cx_Oracle.version)
#参数：用户名/密码@监听(server主机：server端口/server名称)
#配置监听
username = "yl2012"
userpwd = "yl.Q.ACL"
host = "192.168.1.210"
port = '1104'
dbname = "db228"


#tns=cx_Oracle.makedsn('host',1521,'orcl')
# tns=cx_Oracle.makedsn('192.168.1.210','1104','db228')
tnsq=cx_Oracle.makedsn(host,port,dbname)
#
# #用户名、密码、TSN,设置字符编码
con=cx_Oracle.connect(username,userpwd,tnsq)
#创建xursor
cursor=con.cursor()
sql=' select * from t_address t where t.customersid = 61713471  '
rr=cursor.execute (sql)
TT=cursor.fetchone()
print(TT)

#print(rr)

