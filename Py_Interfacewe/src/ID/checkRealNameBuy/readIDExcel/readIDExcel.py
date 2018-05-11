import xlrd
import sys


class readExcel(object):
   def __init__(self,path):
        self.path = path


   @property
   def getSheet(self):
         # 获取索引
         xl = xlrd.open_workbook(self.path)
         sheet = xl.sheet_by_index(0)
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
   def getcardType(self):
       cardType = []
       for i in range(1, self.getRows):
           cardType.append(self.getSheet.cell_value(i,0))
       return cardType

   @property
   def getcardNo(self):
       cardNo = []
       for i in range(1, self.getRows):
           cardNo.append(self.getSheet.cell_value(i,1))
       return cardNo

   @property
   def getproductId(self):
       productId = []
       for i in range(1, self.getRows):
           productId.append(self.getSheet.cell_value(i,2))
       return productId

   @property
   def getrealName(self):
       realName = []
       for i in range(1, self.getRows):
           realName.append(self.getSheet.cell_value(i,3))
       return realName

   @property
   def getthirdVid(self):
       thirdVid = []
       for i in range(1, self.getRows):
           thirdVid.append(self.getSheet.cell_value(i,4))
       return thirdVid


