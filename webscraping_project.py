from urllib.request import urlopen
from bs4 import BeautifulSoup
import openpyxl as xl
from openpyxl.styles import Font


webpage = 'https://cryptoslate.com/coins/'

page = urlopen(webpage)			

soup = BeautifulSoup(page, 'html.parser')

title = soup.title

crypto_table = soup.find('table')

crypto_rows = crypto_table.findAll('tr')

wb = xl.Workbook()

ws = wb.active

ws.title = 'TopCryptoReport'


ws['A1'] = 'Name'
ws['B1'] = 'Symbol'
ws['C1'] = 'Price'
ws['D1'] = '24 Hour Percent Change'
ws['E1'] = '24 Hour Value Change'

