import sqlite3
import pandas as pd

# substitute username with your username
conn = sqlite3.connect('chat.db')
# connect to the database
cur = conn.cursor()
# get the names of the tables in the database
cur.execute(" select name from sqlite_master where type = 'table' ") 

# sql command
SQL = """
SELECT datetime(message.date/1000000000 + strftime("%s", "2001-01-01") ,"unixepoch","localtime") AS date_uct, id, text, is_from_me
FROM message
LEFT JOIN handle
ON message.handle_id = handle.ROWID
WHERE id='[number]' AND text LIKE '%hi%' 
"""

# get messages using the sql
messages = pd.read_sql_query(SQL, conn)

print(messages) # not the best way to print because you only see a few
