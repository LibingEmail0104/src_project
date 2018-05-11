#_*_coding: utf-8 _*_
import xlrd
#方法一
# data =xlrd.open_workbook('E:\工作记录\文档\src_project\TEST.xlsx') #打开文件
# table =data.sheets()[0] #读取excel的第一sheets
# nrows =table.nrows      #计算列数
#
# for i in range(nrows):
#     if i== 0 :
#         continue
#     print(table.row_values(i))


#方法二  全部读取sheeet  根据名称读取
workbook =xlrd.open_workbook('E:\工作记录\文档\src_project\TEST1.xlsx')

# 抓取所有sheet页面名称
sheetsname=workbook.sheet_names()
print("sheet页名是%s" %sheetsname)

#定位自己的sheet
worksheet=workbook.sheet_by_name(u'Sheet2')

#遍历所有的行
nrow2=worksheet.nrows

for i in range(nrow2):
    value=worksheet.row_values(i)
    print('行数是%s ，内容是%s' %(i,value))

#遍历所有的列

cols=worksheet.ncols

for A in range(cols):
    valuecol=worksheet.col_values(A)
    print('列数是%s,内容是%s' %(A,valuecol))

#全部读取内容  遍历所有的单元格cell

for rown in range(nrow2):
    for coln in range(cols):
        if rown ==0 :
            continue

        cell=worksheet.cell_value(rown,coln)
        print('这里是Excel的全部内容%s' %cell)
    print('=================')


