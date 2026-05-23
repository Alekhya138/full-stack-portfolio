import sqlite3

conn = sqlite3.connect("portfolio.db")

rows = conn.execute("SELECT * FROM messages").fetchall()

for row in rows:
    print(row)

conn.close()