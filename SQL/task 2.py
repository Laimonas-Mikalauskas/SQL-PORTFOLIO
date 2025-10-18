# Task 1

import sqlite3

conn = sqlite3.connect('super_db.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS people (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    INSERT number TEXT,
    INSERT name TEXT
)
""")

# Task 2

import sqlite3

conn = sqlite3.connect('super_db.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS people (
    id INTEGER PRIMARY KEY AUTOINCREMENT
    INSERT number TEXT,
    INSERT number TEXT,
)
""")


