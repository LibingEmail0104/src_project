import xlrd
import sys


class readExcel(object):
   def __init__(self,path):
        self.path = path


   @property
   def getSheet(self):
         # 获取索引
         xl = xlrd.open_workbook(self.path)
         sheet = xl.sheet_by_index(2)
         return sheet

   @property
   def getRows(self):
        # 获取行数
         row = self.getSheet.nrows
         return row

   @property
   def getCol(self):
         # 获取列数
        col = self.getSheet.ncols
        return col
      # 以下是分别获取每一列的数值


   @property
   def getNO(self):
       TestNO = []
       for i in range(1, self.getRows):
           TestNO.append(self.getSheet.cell_value(i,0))
       return TestNO

   @property
   def getinfo(self):
       info = []
       for i in range(1, self.getRows):
           info.append(self.getSheet.cell_value(i,1))
       return info

   @property
   def getname(self):
        getname = []
        for i in range(1, self.getRows):
            getname.append(self.getSheet.cell_value(i,2))
        return getname

   @property
   def getcertType(self):
        certType = []
        for i in range(1, self.getRows):
            certType.append(self.getSheet.cell_value(i,3))
        return certType

   @property
   def getcertNo(self):
         certNo = []
         for i in range(1, self.getRows):
             certNo.append(self.getSheet.cell_value(i,4))
         return certNo

   @property
   def getphone(self):
         phone = []
         for i in range(1, self.getRows):
             phone.append(self.getSheet.cell_value(i,5))
         return phone

   @property
   def getcardNo(self):
        cardNo = []
        for i in range(1, self.getRows):
            cardNo.append(self.getSheet.cell_value(i,6))
        return cardNo

   @property
   def getcardType(self):
       cardType = []
       for i in range(1, self.getRows):
           cardType.append(self.getSheet.cell_value(i,7))
       return cardType

   @property
   def getcustomerId(self):
       customerId = []
       for i in range(1, self.getRows):
           customerId.append(self.getSheet.cell_value(i,8))
       return customerId

   @property
   def getsign(self):
       sign = []
       for i in range(1, self.getRows):
           sign.append(self.getSheet.cell_value(i,9))
       return sign

   @property
   def getverify(self):
       verify = []
       for i in range(1, self.getRows):
           verify.append(self.getSheet.cell_value(i,10))
       return verify

   @property
   def geturl(self):
       url = []
       for i in range(1, self.getRows):
           url.append(self.getSheet.cell_value(i,11))
       return url

   @property
   def getmethod(self):
       method = []
       for i in range(1, self.getRows):
           method.append(self.getSheet.cell_value(i,12))
       return method