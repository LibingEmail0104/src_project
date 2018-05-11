# coding=utf-8
import requests
import unittest
import json


url="http://192.168.1.88:8051/order/create/general.json"

#票纸类型
#tickettype=2
#采购信息
#purchasese=[{"cashno":"","cityid":1,"cityname":"北京市","insurance":0,"renewal":"0.0","shipment":1,"tickets":"20219361^1"}]
#用户ID
#customerid=61713471
#地址ID
#addressid=12083070
#订单来源
#origin=4
#支付方式
#payid=2217200
#商品类型-在线选座-特殊电子票-先付先抢
#type="general"
#购票信息
#ticketse=20219361^1
#
#loginType=0

class purchase:
    "初始化"
    def __int__(self):
        self.cashno=""
        self.cityid=1
        self.cityname=""
        self.insurance=0
        self.renewal="0.0"
        self.shipment=1
        self.tickets="20219361^1"

purchases=purchase()
purchases.cashno=""
purchases.cityid=1
purchases.cityname="北京市"
purchases.insurance=0
purchases.renewal="0.0"
purchases.shipment=1
purchases.tickets="20219361^1"
#对象转化成字典再转化成json
purchasesdic=purchases.__dict__
purchasesjson=json.dumps(purchasesdic)

purchas=[purchasesjson]


class date:
    "date请求数据"
    def __int__(self):
        self.tickettype=0
        self.purchases=0
        self.customerid=0
        self.addressid=0
        self.origin=4
        self.payid=0
        self.type=""
        self.ticketse=0
        self.loginType=0

datee=date()

datee.tickettype=1
datee.purchases=purchas
datee.customerid=61713471
datee.addressid=12083070
datee.origin=4
datee.payid=2217200
datee.type="general"
datee.ticketse=20219361^1
datee.loginType=0

datajson=json.dumps(datee)



print(datajson)

print(purchasesjson)



