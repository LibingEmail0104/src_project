#coging=utf-8
import hashlib
import requests
import json



s="123234"
s1="522101197403216410"
s2="测试"
s3="1231234fd23"+"123234"
m=hashlib.md5()
m.update(s3.encode(encoding="utf-8"))
print(m.hexdigest())






#待加密信息
card="320925199411036123"
namestr="吴君"
apid="10005"
key="ch7GK1DFlo9F1t4p"
str=namestr+card+key

#创建加密对象
str1=hashlib.md5()
str1.update(str.encode(encoding="utf-8"))
print("加密前："+str)
print("加密后："+str1.hexdigest())
sign1=str1.hexdigest()
print(sign1)


data1=json.dumps(
{
    "app_id":"10005",
    "id_card_no":"320925199411036123",
    "real_name":"吴君",
    "sign":sign1
}
)
herder={
    "host":"riskm.228/api",
    "Content-Type": "application/x-www-form-urlencoded"
}
renzheng=requests.post(url='http://riskm.228/api/realCheck',data=data1)
print(renzheng.text)

