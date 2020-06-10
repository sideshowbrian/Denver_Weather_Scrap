"""
Created on Wed June 1, 2020
working as of June xx, 2020

@author: brian
"""

import sqlite3
import Ch2, Ch7, Ch9

# Create a connection to the sqlite server
#conn = sqlite3.connect('Weather.sqlite')
conn = sqlite3.connect('/home/pi/Python/Weather/Weather.sqlite')
cur = conn.cursor()

data2 = Ch2.weather()

print('channel 2')
cur.executemany('''
INSERT OR REPLACE INTO Main VALUES (NULL,?,?,?,?,?)''', data2)
conn.commit()

data7 = Ch7.weather()

print('channel 7')
cur.executemany('''
INSERT OR REPLACE INTO Main VALUES (NULL,?,?,?,?,?)''', 
data7)
conn.commit()

data9 = Ch9.weather()

print('channel 9')
cur.executemany('''
INSERT OR REPLACE INTO Main VALUES (NULL,?,?,?,?,?)''', 
data9)
conn.commit()

