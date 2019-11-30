import xlrd
import xlwt
import re

x1 = xlrd.open_workbook(r'D:\SRT数据\drugbank\eseq_interactions.xlsx')
sheet = x1.sheet_by_name('eseq_interactions')

interation = sheet.col_values(5,1)
drug_interation = []
f = xlwt.Workbook()
sheet1 = f.add_sheet(u'sheet1', cell_overwrite_ok=True)  # 创建sheet
for i in range(len(interation)):
    list = re.findall('【(.*?)】',interation[i])
    interation[i] = interation[i].replace('【', '')
    interation[i] = interation[i].replace('】', '')
    list.append(interation[i])
    for k in range(len(list)):
        sheet1.write(i, k, list[k])

f.save('药物关系.xls')

