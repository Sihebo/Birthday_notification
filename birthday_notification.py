

import sqlite3
from sqlite3 import Error
import os
import datetime
import telebot
#from telebot import types



# Connect to DB


def create_connection(path):  # Function to create DB and create connection
    connection = None
    try:
        connection = sqlite3.connect(path)
        #print("Connection to SQLite DB successful.")
    except Error as e:
        print(f"The error '{e}' occurred.")

    return connection

# Connect to DB and create connection variable.
connection = create_connection("/home/simon/Schreibtisch/Python_Projects/Birthday_script/Database/Birthday_DB.sqlite")


# Get current date (mm-dd) and store it in variable 'date'.

today = datetime.datetime.today()

date = today.strftime("%m-%d")

date = '%' + date + '%'

#print(date)

# Make a DB query with current date. If entry found, store in variable.

cursor = connection.cursor()
d = (date,)
cursor.execute('SELECT * FROM birthdays WHERE birth_data like (?);', d)
DB_entries = cursor.fetchall()

#print(DB_entries)
#print(DB_entries)
#for entry in DB_entries:
#    print(entry)

# Print a message with name, birthdate and age to inform about birthday.

def birthday_message(DB_list):
    list = []
    if not DB_list:
        return None
    else:
        for entry in DB_list:
            name = entry[0]
            birthdate = entry[1]
            birthyear = birthdate[:4]
            Current_year = today.year
            Age = int(Current_year) - int(birthyear)
            list.append("Today is "+ name + "`s birthday (" + str(birthdate) + "). It`s the " + str(Age) + "th.")
        return list

function_list = birthday_message(DB_entries)




# Automatically send Telegram message with notification in case there is a birthday.
TOKEN = ''
tb = telebot.TeleBot(TOKEN)
tb.config['api_key'] = TOKEN
tb.get_updates()
if not function_list:
    pass
else:
    for i in function_list:
        #print(i)
        tb.send_message(chat_id ='', text=i)


# Automatically startup when Ubuntu is started, once a day.
