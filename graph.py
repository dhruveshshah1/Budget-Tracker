import sqlite3
import time
import datetime
import random
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from dateutil import parser
from matplotlib import style
style.use('fivethirtyeight')

conn = sqlite3.connect('stuffToPlot.db')
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL, datestamp TEXT, keyword TEXT, value REAL)")


def data_entry():
    c.execute("INSERT INTO stuffToPlot VALUES(1452549219,'2016-01-11 13:53:39','Python',6)")
    
    conn.commit()
    

def dynamic_data_entry():

    unix = int(time.time())
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    keyword = 'Python'
    value = random.randrange(0,10)

    c.execute("INSERT INTO stuffToPlot (unix, datestamp, keyword, value) VALUES (?, ?, ?, ?)",
          (unix, date, keyword, value))

    conn.commit()
    time.sleep(1)

def read_from_db():
    c.execute('SELECT * FROM stuffToPlot')
    data = c.fetchall()
    print(data)
    for row in data:
        print(row)

    c.execute('SELECT * FROM stuffToPlot WHERE value = 3')
    data = c.fetchall()
    print(data)
    for row in data:
        print(row)

    c.execute('SELECT * FROM stuffToPlot WHERE unix > 1452554972')
    data = c.fetchall()
    print(data)
    for row in data:
        print(row)

    c.execute('SELECT value, datestamp FROM stuffToPlot WHERE unix > 1452554972')
    data = c.fetchall()
    print(data)
    for row in data:
        print(row[0])
    


def graph_data():
    c.execute('SELECT datestamp, value FROM stuffToPlot')
    data = c.fetchall()

    dates = []
    values = []
    
    for row in data:
        dates.append(parser.parse(row[0]))
        values.append(row[1])

    plt.plot_date(dates,values,'-')
    plt.show()
create_table()
data_entry()
dynamic_data_entry()
read_from_db()
graph_data()
