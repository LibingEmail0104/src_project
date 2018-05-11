
from src.guanda.read_xl.readExcel import readExcel
from src.request_api.testapi import testapi
e=readExcel(r'E:\工作记录\文档\接口\接口文档\永乐\PoiExcel\28光大银行\光大银行(测试环境).xlsx')
row=e.getRows
col=e.getCol
No=e.getNO
info=e.getinfo
name=e.getname
certType=e.getcertType
certNo=e.getcertNo
phone=e.getphone
cardNo=e.getcardNo
cardType=e.getcardType
customerId=e.getcustomerId
sign=e.getsign
verify=e.getverify
url=e.geturl
method=e.getmethod
print(col)




# print(method)
#
#
# date={
#
#  "name":"陈广荣",
#  "certType":"1",
#  "certNo":"320102197910131611",
#  "phone":"13911108822"
# }
# api=testapi("post","http://192.168.1.88:8051/order/create/general.json",date)
# a=api.getcode()
# b=api.getjson()
#
# print(a,b)

for i in range(0,row-1):

    datt = {'name':name[i],
            'certType':certType[i],
            'certNo':certNo[i],
            'phone':phone[i],
            'cardNo':cardNo[i],
            'cardType':cardType[i],
            'customerId':customerId[i],
            'sign':sign[i]}

    api=testapi(method[i],url[i],datt)
    #
    #
    apipicode=api.getcode()
    apiinfo=api.getjson()
    print(apipicode)
    print(apiinfo)
    print(name[i])

    if apiinfo==verify[i]:
      print('{}、{}:测试成功。json数据为:{}'.format(i + 1,info[i],apiinfo))
      continue
    else:
      print('{}、{}:测试失败'.format(i + 1, info[i]))
      print('{}、{}：预期结果'.format(i + 1, verify[i]))
      print('{}、{}：实际返回结果'.format( i+ 1,apiinfo))
      continue
