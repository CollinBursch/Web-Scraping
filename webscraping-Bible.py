import random
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

chapters = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10']

random_chapter = random.choice(chapters)

url = 'https://ebible.org/asv/JHN' + random_chapter + '.htm'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(url, headers=headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

all_verses = soup.findAll('div', class_='p')

all_verses = all_verses.findAll('span')
print(all_verses.text)

'''

myverses = []

for verse in all_verses:
    #print(verse.text.split('  '))
    for v in verse.text.split('  ')):
        myverses.append[v]

mychoice = random.choice(myverses)

print('Chapter: ', random_chapter, 'Verse: ', mychoice)

'''
