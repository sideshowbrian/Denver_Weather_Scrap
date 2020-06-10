# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 16:57:42 2019
Working May 21, 2020

@author: brian
"""
from bs4 import BeautifulSoup
import datetime
#from urllib2 import urlopen
import requests

def weather():
    #7news site
    ch7news = "https://www.thedenverchannel.com/weather/daily-forecast"

    # query the website and return the html to the variable ‘page’
    #ch7news_page = urlopen(ch7news)
    ch7news_page = requests.get(ch7news)

    #use beautifulsoup to convert the page
    soup = BeautifulSoup(ch7news_page.text, 'html.parser')

    #pull the temps from 7news
    Daily_weather = soup.select("p.temp-ext")

    #pull the forecast date
    Forecast_Date = soup.select("p.fore-date")
    today = datetime.date.today()
    data = []
    for i in range(0,6):
        date = Forecast_Date[i].get_text()
        #remove the space at the end of the string
        date = date[:-1]
        
        #pull weather string
        raw_temp  = Daily_weather[i+1].get_text()

        #split off the low temp, remove the degree sign, convert to int
        temp = int(raw_temp.split()[0][:-1])
        ch = "Ch7"
        data.append((ch, date, temp, i, today.strftime("%m/%d/%Y")))
    return data
