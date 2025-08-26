import sqlite3

conn = sqlite3.connect("books.db")
c = conn.cursor()

with sqlite3.connect("books.db") as conn:
    c = conn.cursor()
    c.execute("INSERT INTO knygos VALUES (?, ?, ?, ?)",
              ("Žiedų valdovas: Žiedo brolija", "Fantastika", 1954, "J.R.R. Tolkien"))
    c.execute("INSERT INTO knygos VALUES (?, ?, ?, ?)",
              ("Žiedų valdovas: Dviejų tvirtovių", "Fantastika", 1954, "J.R.R. Tolkien"))
    c.execute("INSERT INTO knygos VALUES (?, ?, ?, ?)",
              ("Žiedų valdovas: Karaliaus sugrįžimas", "Fantastika", 1955, "J.R.R. Tolkien"))

c.execute("INSERT INTO knygos VALUES (?, ?, ?, ?)",
          ("Hobitas", "Fantastika", 1937, "J.R.R. Tolkien"))
c.execute("INSERT INTO knygos VALUES (?, ?, ?, ?)",
          ("Silmariljonas", "Fantastika", 1977, "J.R.R. Tolkien"))

conn.commit()
conn.close()