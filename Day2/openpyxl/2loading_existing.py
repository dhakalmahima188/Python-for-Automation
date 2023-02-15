from openpyxl import load_workbook
from openpyxl.utils import get_column_letter
####loading a existing workbook
wb = load_workbook('begin.xlsx')
ws = wb.active

########creating a new sheet##########

wb.create_sheet('new sheet')
ws.title = 'sample1'
print(ws.title)
print(wb.sheetnames)
ws1 = wb['new sheet']

for row in range(1, 11):
    for col in range (1, 5):
        char = get_column_letter(col)
        ws1[char + str(row)]= char + str(row)
wb.save('test2.xlsx')

