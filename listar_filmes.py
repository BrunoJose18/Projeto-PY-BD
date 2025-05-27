import sqlite3

conn = sqlite3.connect('oscar.db')
cursor = conn.cursor()

cursor.execute("SELECT id, titulo FROM Filmes LIMIT 20")
for row in cursor.fetchall():
    print(row)

conn.close()
