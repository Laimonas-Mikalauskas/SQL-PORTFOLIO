import sqlite3

conn = sqlite3.connect("employees.db")
c = conn.cursor()

c.execute ('''
      CREATE TABLE IF NOT EXISTS employees (''
      name Tom, 
      surname Gordon,
      role Python developer,
      salary 2000,
      experience 2 years  
'')
''')
conn.commit()
conn.close()
''')
'''



