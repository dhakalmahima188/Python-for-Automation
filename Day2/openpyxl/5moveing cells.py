from openpyxl import load_workbook

wb = load_workbook('range.xlsx')
ws = wb.active
ws.move_range("A1:B2",rows= 5, cols = 5)
wb.save('range.xlsx')
