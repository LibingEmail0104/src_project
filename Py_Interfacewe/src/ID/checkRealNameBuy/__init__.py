import requests


date={

 "name":"陈广荣",
 "certType":"1",
 "certNo":"320102197910131611",
 "phone":"13911108822"



}
e=requests.post("http://192.168.1.88:8051/order/create/general.json",data=date)
print(e.text)