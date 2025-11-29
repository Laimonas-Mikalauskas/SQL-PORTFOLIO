import sqlite3

conn = sqlite3.connect("employees.db")
c = conn.cursor()

# Correct SQL CREATE TABLE statement

c.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        name Tom,
        surname Gordon,
        role Python developer,
        salary INTEGER
        experience INTEGER
    )
''')

# Add a row with integer salary (just the number, no type keyword)
c.execute('''
    INSERT INTO employees (name, surname, role, salary, experience)
    VALUES (?, ?, ?, ?, ?)
''', ('Tom', 'Gordon', 'Python developer', 2000, '2 years'))


conn.commit()
conn.close()
