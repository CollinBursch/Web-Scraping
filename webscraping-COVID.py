# pip install requests (to be able to get HTML pages and load them into Python)
# pip install bs4 (for beautifulsoup - python tool to parse HTML)

'''
<> are called tags 
<> <> whatever is in between tags can be extracted 
<span class = </span>
<h1> 28.91 </h1>
<p> </p>

'''
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup


##############FOR MACS THAT HAVE ERRORS LOOK HERE################
## https://timonweb.com/tutorials/fixing-certificate_verify_failed-error-when-trying-requests_html-out-on-mac/

############## ALTERNATIVELY IF PASSWORD IS AN ISSUE FOR MAC USERS ########################
##  > cd "/Applications/Python 3.6/"
##  > sudo "./Install Certificates.command"



url = 'https://www.worldometers.info/coronavirus/country/us'
# Request in case 404 Forbidden error
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}


req = Request(url, headers=headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage,'html.parser')

title = soup.title

print(title.text)

table_rows = soup.findAll('tr')

state_death_ratio = ''
state_beat_testing = ''
state_worst_testing = ''
highest_death_ratio = ''
high_test_ratio = 0.0
low_test_ratio = 0.0


for row in table_rows[2:51]:
    td = row.findAll('td')

    state = td[1].text
    total_cases = int(td[2].text.replace(',',''))
    total_deaths = int(td[4].text.replace(',',''))
    total_tested = int(td[10].text.replace(',',''))

    '''
    print(f'State: {state}')
    print(f'Total Cases: {total_cases}')
    print(f'Total Deaths: {total_death}')
    print(f'Total Tested: {total_tested}')
    '''

    death_ratio = total_deaths / highest_death_ratio
    test_ratio = total_cases / total_tested

    if death_ratio > highest_death_ratio:
        state_death_ratio = state
        highest_death_ratio = death_ratio
    
    if test_ratio > high_test_ratio:
        state_worst_testing = state
        high_test_ratio = test_ratio

    if test_ratio < low_test_ratio:
        state_beat_testing = state
        low_test_ratio = test_ratio

    print()


#SOME USEFUL FUNCTIONS IN BEAUTIFULSOUP
#-----------------------------------------------#
# find(tag, attributes, recursive, text, keywords)
# findAll(tag, attributes, recursive, text, limit, keywords)

#Tags: find("h1","h2","h3", etc.)
#Attributes: find("span", {"class":{"green","red"}})
#Text: nameList = Objfind(text="the prince")
#Limit = find with limit of 1
#keyword: allText = Obj.find(id="title",class="text")

