import sqlite3

conn = sqlite3.connect('interior.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM contacts")
data = cursor.fetchall()

for row in data:
    print(row)

conn.close()