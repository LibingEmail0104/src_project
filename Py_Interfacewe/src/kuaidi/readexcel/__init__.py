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