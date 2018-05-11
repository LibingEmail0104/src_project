import requests
import json

da={
    'idCardNo':'142232199211182194',
    'realName':'王志军',
    'customerId':'61713471'
}
r=requests.post('http://192.168.1.88:8051/verify/riskManagement',data=da)
ajson=r.json()
#alljson=json.loads(ajson)

print(ajson)

print(ajson['code'])