import  requests
import  json

class testapi(object):

    def __init__(self,method,url,data):
        self.method=method
        self.url=url
        self.data=data
    @property
    def testapitry(self):
        "根据不同的方式请求访问接口"
        try:
            if self.method=="post":
                r=requests.post(self.url,data=json.dumps(self.data))

                print("接口请求方式==》post")
            elif self.method=="get":
                r=requests.get(self.url,params=eval(self.data))
                print("接口请求方式==》get")

            return r
        except:
            print("api访问接口失败")

    def getcode(self):
        "获取访问接口的状态码"
        #code=self.testapitry.json()["error"]
        code=self.testapitry.status_code
        return code
    def getjson(self):
        "获取访问接口的返回信息"
        #json_data=self.testapitry.json()
        json_data=self.testapitry.text
        return json_data
