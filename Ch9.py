# -*- coding: utf-8 -*-
"""
Created on Wed May 3, 2020
working as of May 5, 2020

@author: brian
"""
from bs4 import BeautifulSoup
#from urllib2 import urlopen
import requests
import datetime  
from datetime import timedelta  

def weather():
    #7news site
    ch9news = "https://www.9news.com/10-day"

    # query the website and return the html to the variable ‘page’
    ch9news_page = requests.get(ch9news)

    #use beautifulsoup to convert the page
    soup = BeautifulSoup(ch9news_page.text, 'html.parser')

    #pull the temps from 7news
    Daily_weather = soup.select("div.weather-10-day__temperature-high")

    #pull the forecast date
    month = "weather-10-day__month weather-10-day__month_visible_true" 
    Forecast_month = soup.find_all('span',attrs={"class" : month})

    day = "weather-10-day__date weather-10-day__date_visible_true" 
    Forecast_day = soup.find_all('span',attrs={"class" : day})

    #calculate the difference between today and forecast date
    datetime_object = datetime.datetime.now()
    Time_shift = int(Forecast_day[0].get_text()) - datetime_object.day
    today = datetime.date.today()
    data = []
    for i in range(1,7):
        date = datetime.date.today() + timedelta(days = (i+Time_shift))
        date = date.strftime("%m/%d/%Y")

        temp = int(Daily_weather[i].get_text())
        ch = "Ch9"

        data.append((ch, date, temp, i, today.strftime("%m/%d/%Y")))
    return data

