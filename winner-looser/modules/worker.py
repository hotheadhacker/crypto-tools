# This is the main file contains all necessary function to run overall program 
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import urllib
from urllib.request import Request, urlopen
import pandas as pd
import lxml
import random

# for getting over all market growth
def getOverallMarketTrend():
    rand = random.random() #To overide cache
    URL = 'https://www.coinbase.com/price/s/top-gainers?v=' + str(rand)
    req = Request(URL , headers={'User-Agent': 'Mozilla/5.0'})
    page = urlopen(req).read()
    soup = BeautifulSoup(page, 'html.parser')

    results = soup.find(class_="MarketHealth__Value-sc-1a64a42-3")
    
    return(results.text)
    # return("🚀 The Market is Up 24% From Last 24 hrs 📈")


# For Getting top winner coins
def losers():
    print("Losers in last 24 hrs")
    URL = 'https://coincodex.com/gainers-losers/'
    req = Request(URL , headers={'User-Agent': 'Mozilla/5.0'})
    page = urlopen(req).read()
    soup = BeautifulSoup(page, 'html.parser')
    table = soup.find_all('table', attrs={'class':'coins'})
    # table_body = table.find('tbody')
    data = table[1].find_all('tr')
    for el in data:
        cols = el.find_all('td')
        temp = ""
        print("======+++++++++++++++++++============")
        for td in cols:
            temp += td.text + " "
        print(temp)
    # data = table[0]
    # df_list = pd.read_html(soup) # this parses all the tables in webpages to a list
    # df = df_list[0]
    # df.head()
    # print(df)


def winners():
    print("Winners in last 24 hrs")

    url = "https://coincodex.com/gainers-losers/"

    r = requests.get(url)
    df_list = pd.read_html(r.text) # this parses all the tables in webpages to a list
    df = df_list[0]
    df.head()
    print(df)