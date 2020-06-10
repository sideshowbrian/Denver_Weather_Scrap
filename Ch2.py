# -*- coding: utf-8 -*-
"""
Created on May 21, 2020
Working May 21, 2020

@author: brian
"""
from bs4 import BeautifulSoup
import datetime
#from urllib2 import urlopen
import requests

def weather():
    #7news site
    kdvr_news = "https://kdvr.com/weather/"

    # query the website and return the html to the variable ‘page’
    #kdvr_news_page = urlopen(kdvr_news)
    kdvr_news_page = requests.get(kdvr_news)

    #use beautifulsoup to convert the page
    soup = BeautifulSoup(kdvr_news_page.text, 'html.parser')

    #pull the temps from 7news
    Daily_weather = soup.select("span.high")

    #pull the forecast date
    Forecast_Date = soup.select("h4.day")

    #find the name of today
    today = datetime.date.today()

    data = []
    #loop through the data collected for each day
    for i in range(0,6):
        date = today + datetime.timedelta(i)
        
        #check to see if the date is correct by matching day names
        if Forecast_Date[i].get_text() != date.strftime('%A'):
            print('day is not matching, %s is not %s'
            % (Forecast_Date[i].get_text(),  date.strftime('%A')))
            continue

        # spaces need to be stripped out of the text
        temp = Daily_weather[i].get_text()
        temp = temp.strip() 

        #strip off the degree sign and convert to int
        temp = int(temp[:-1])
        ch = 'Ch2-31'
        data.append((ch, date.strftime("%m/%d/%y"), temp, i, 
        today.strftime("%m/%d/%Y")))
        

    return data

