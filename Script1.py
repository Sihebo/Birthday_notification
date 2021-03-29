# First script to create SQLite database and table storing database

# Create database here

import sqlite3
from sqlite3 import Error


def create_connection(path):  # Function to create DB and create connection
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful.")
    except Error as e:
        print(f"The error '{e}' occurred.")

    return connection

# Call function to create connection to DB or create DB
connection = create_connection("path_to_DB/Birthday_DB.sqlite")


# Create DB table storing data
def execute_query(connection, query): # Method to create tables and execute queries
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed succesfully.")
    except Error as e:
        print(f"The error '{e}' occurred.")


# Query to create table
create_birthday_table = """
CREATE TABLE IF NOT EXISTS birthdays (
name TEXT NOT NULL,
birth_data TEXT NOT NULL,
relation TEXT NOT NULL
)
"""

# Create table with execute Method
execute_query(connection, create_birthday_table)
