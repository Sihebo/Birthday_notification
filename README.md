# Birthday_notification
Script to automatically send birthday notifications via a Telegram bot.

Script1.py
  Creates SQLite3 DB consisting of one table, which contains name, birthdate and relation status.
  
Scritp2.py
  Script to add new entries to the DB, delete entries and get an overview of all existing entries via a simple terminal menu.

 birthday_notification.py
  Queries SQLite3 DB for birthday entries of current day and sends a short message using a Telegram bot with name, age and birthdate.
