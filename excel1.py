import openpyxl as xl
from openpyxl.styles import Font


#create a new excel document
wb = xl.Workbook()

MySheet = wb.active

MySheet.title = 'First Sheet'

wb.save('PythonToExcel.xlsx')

#create a new worksheet 
wb.create_sheet(index=1, title='Second Sheet')

#write content to a call
MySheet['A1'] = 'An Example of Sum Formula'

#change the forn size and italicize
MySheet['A1'].font = Font(name= 'Times New Roman', size=24, italic=True, bold=True)

#alternatively you can creeate a Font object and assign it 
fontobject = Font(name= 'Times New Roman', size=24, italic=True, bold=True)

MySheet['A1'].font = fontobject

#adding values to cells
MySheet['B2'] = 50
MySheet['B3'] = 75
MySheet['B4'] = 100

MySheet['A6'] = 'Total'
MySheet['A6'].font = Font(size=16, bold=True)

MySheet['B6'] = '=SUM(B2:B4)'

#change the column width
MySheet.column_dimensions['A'].width = 25

wb.save('PythonToExcel.xlsx')