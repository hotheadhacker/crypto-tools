import requests
from bs4 import BeautifulSoup
from datetime import datetime
import json
import urllib


URL = 'https://www.greaterkashmir.com/latest/'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
    # print(soup)

    # Finding result
results = soup.find(id='main')

news = results.find_all('h2', class_='m-article-first-large-listing__title')

    # creating response array
data_list = []
    #Get time

    

i = 0
    # print(news)
for item in news:
    i = i+1
        # making it neet
        # print("Reading Next News")
        # print(item)
    # title = "<h2>" + item.text + "</h2>"
    
    item_link = item.find('a')
    link = item_link.get('href')
    # link2 = item_link.get('href')
    print(link)
    # urllib.parse.urlencode(link)
    new_link = link.replace("https://", "detailArticle/?url=")
    new_link = "<h2><a href='" + new_link + "'>" + str(i)+") "+ item.text + "</a></h2>"
    data_list.append([new_link])
    # print(data_list)
    
    
# load_gk()