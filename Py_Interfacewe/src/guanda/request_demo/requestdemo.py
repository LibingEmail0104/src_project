import unittest
from src.guanda.read_xl import readExcel
from src.request_api.testapi import testapi
print("efwef")
class requestdemo(unittest.TestCase):
    "调用接口开始"
    print("scscsdsdcdsd")
    def requestde(self):


        e=readExcel(r'C:\Users\yl\Desktop\永乐\PoiExcel\28光大银行\光大银行(测试环境).xlsx')
        row=e.getRows
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



        print('efwefew')
        print(url)
        for i in range(0,row-1):
            api=testapi(method=method[i],url=url[i],data=(name[i],certType[i],certNo[i],phone[i],cardNo[i],cardType[i],customerId[i],sign[i]))
            apicode=api.getcode()
            apijson=api.getjson()

            if apicode==verify[i]:
                print('{}、{}:测试成功。json数据为:{}'.format(i + 1, name[i], apijson))
            else:

                print('{}、{}:测试失败'.format(i + 1, name[i]))

if __name__=='__main__':
    unittest.main(verbosity=2)


