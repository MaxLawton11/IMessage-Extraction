import sqlite3
import pandas as pd

conn = sqlite3.connect('chat.db')
cur = conn.cursor()

# Get all tables
tables = cur.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()

for table in tables:
    table_name = table[0]
    print(f"\nColumns in table '{table_name}':")
    columns = cur.execute(f"PRAGMA table_info({table_name})").fetchall()
    for col in columns:
        print(f" - {col[1]} ({col[2]})")
