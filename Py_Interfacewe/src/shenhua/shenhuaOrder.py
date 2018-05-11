# _*_ coding: utf-8 _*_
import requests
import unittest
#post请求链接地址


# shenhuaURL='http://192.168.1.88:8051/order/create/shenhua.do'
# shenhuaparms={
#     'productid':'19390121',
#     'season':'2019',
#     'playids':'1280,1980,2680;19390543,19390544,19390545',
#     'cardType':'1,2',
#     'organize':'1,2,3,4,5,6,7,8,9,10'
# }
#
# r=requests.post(shenhuaURL,data=shenhuaparms,json=None)
# print(r.text)
class shenhuaorderapi(unittest.TestCase):
    def setUp(self):
        self.shenhuaURL = 'http://192.168.1.88:8051/order/create/shenhua.do'
        self.headers={
            
        }
    def shenhuadata(self):
        shenhuaparms = {

            'productid':'19390121',
            'season':'2019',
            'playids':'1280,1980,2680;19390543,19390544,19390545',
            'cardType':'1,2',
            'organize':'1,2,3,4,5,6,7,8,9,10'
         }
        shenhuaURL = 'http://192.168.1.88:8051/order/create/shenhua.do'



        r=requests.post(shenhuaURL,data=shenhuaparms)
        print("wefwf")
    def tearDown(self):
        pass

if __name__=='__main__':
    unittest.main()
