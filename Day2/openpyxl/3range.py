from openpyxl import Workbook
wb = Workbook()
ws = wb.active
x = 1

cell_range = ws['A1':'C2']
for row in ws.iter_rows(min_row=1, max_col=3, max_row=2):
    for cell in row:
        x= x+1
        cell.value = x
        print(cell.value)

wb.save('range.xlsx')
