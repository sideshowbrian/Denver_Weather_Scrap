"""
Created on Wed June 1, 2020
working as of June xx, 2020

@author: brian
"""

import sqlite3

# Create a connection to the sqlite server
conn = sqlite3.connect('Weather.sqlite')
cur = conn.cursor()


def build_table_main():
    cur.executescript('''
    CREATE TABLE IF NOT EXISTS Main (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        station TEXT,
        forecast_date TEXT,
        high_temp TEXT,
        forecast_days_out TEXT,
        date_time_pulled INTEGER
        )''')
    conn.commit()
    
def drop_main():
	cur.executescript('''DROP TABLE IF EXISTS Main''')
	conn.commit()

def view():
	cur.execute('''SELECT * FROM Main''')
	return cur.fetchall()
	
def remove_data():
	cur.executescript('''DELETE FROM Main WHERE id > 400''')
	conn.commit()

for i in view():
	print(i)
