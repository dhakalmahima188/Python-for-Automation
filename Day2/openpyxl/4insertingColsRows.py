from openpyxl import load_workbook

wb = load_workbook('range.xlsx')
ws = wb.active
ws.insert_rows(2)
#ws.delete_rows(2)
#ws.insert_cols(2)
#ws.delete_cols(2)
wb.save('range.xlsx')
