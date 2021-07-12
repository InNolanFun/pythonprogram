import xlsxwriter
import os
import time

lotime = time.localtime()
todaystr = f'{lotime.tm_year}-{lotime.tm_mon}-{lotime.tm_mday}'
count = 1
filename = f'Export{todaystr}'
while  os.path.exists(f'{filename}_{count}.xlsx'):
    count = count + 1
workbook = xlsxwriter.Workbook(f'{filename}_{count}.xlsx')
workbook.close()

#worksheet = workbook.add_worksheet()
#lst = [
#    ['c1\r\nccc','c2','c3','c4','c5'],
#    ['a1','a2','a3','a4','a5'],
#    ['b1','b2','b3','b4','b5']
#    ]
#
#for i in range(len(lst)):
#    for j in range(len(lst[i])):
#        worksheet.write(i,j,lst[i][j])
