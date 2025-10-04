import sqlite3

conn = sqlite3.connect('library.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS authors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    country TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    year INTEGER,

    author_id INTEGER,
    FOREIGN KEY(author_id) REFERENCES authors(id)
)
""")

cursor.executemany("""
INSERT INTO authors (name, country) VALUES (?, ?)
""", [
    ('Jonas Jonaitis', 'Lithuania'),
    ('Emily', 'USA'),
    ('Haruky', 'Japan')
])

cursor.executemany("""
INSERT INTO books (title, year, author_id) VALUES (?, ?, ?)
""", [
    ('Sun', 2012, 1),
    ('Wind', 2009, 1),
    ('Super code', 2015, 2),
    ('Forest', 2007, 2),
    ('Naruto', 1997, 3),
    ('Sakura', 1998, 3),
    ('Sakura', 1998, 99)
])

conn.commit()

cursor.execute("""
SELECT books.title, books.year, authors.name, authors.country
FROM books, authors
WHERE books.author_id = authors.id
""")

for row in cursor.fetchall():
    print(row)










