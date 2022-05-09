from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

def main():
    # Requesting the html from a web server
    url = 'https://www.imdb.com/chart/top/'
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'})

    # Raw html data
    webpage = urlopen(req).read()		
    # print(webpage[:100])

    # Using BeautifulSoup to turn raw html data into easily searchable data
    soup = BeautifulSoup(webpage, 'html.parser') # Creating beautiful soup object with raw html data, and parsing type
                                                 # Beautiful Soup takes the raw html and makes it easy to access with objects and such
    title = soup.title
    #print(title)

    rating_table = soup.find('tbody') #refers to the body in which you need to look up all the information on the classes you are looking for
                                        # 'find' looks for the first instance of tbody
                                        # 'findall looks for every instance of the class in tbody
    movie_title = rating_table.find_all("td", {"class": "titleColumn"}) # look inside of td and specify which element you want to pull (make sure to mention name of class)
    movie_rating = rating_table.find_all("td", {"class": "ratingColumn imdbRating"}) # 
    for x in range(5):
        print(movie_title[x].find('a').text, movie_rating[x].find('strong').text)

'''
https://i.gyazo.com/374de2cd84251a3f641d53bfd44ac3a4.png
'''
main()