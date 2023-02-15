from openpyxl import Workbook, load_workbook

#loading a existing workbook
#wb = load_workbook('begin.xlsx')

wb = Workbook()

######### grab the active worksheet#########

ws = wb.active
print(ws.title)
ws.title = 'sample1'

########creating a new sheet##########

#wb.create_sheet('new sheet')
#print(wb.sheetnames)


###### Data can be assigned directly to cells####
ws['A1'] = 42

#### Rows can also be appended####
ws.append([1, 2, 3])

######## Python types will automatically be converted######

import datetime
ws['A2'] = datetime.datetime.now()

###########Save the file#########

wb.save("begin.xlsx")
