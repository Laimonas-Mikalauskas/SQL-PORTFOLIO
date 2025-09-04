import sqlite3

# Create table for employees
with sqlite3.connect("employees") as conn:
    c = conn.cursor()
    c.execute ('''
    CREATE TABLE IF NOT EXISTS employees (
        name Tom 
        surname Gordon
        role Python developer
        salary 3000
        experience 2 years  
    )    
''')
conn.commit()
conn.close()
