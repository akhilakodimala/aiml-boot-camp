import sqlite3

conn = sqlite3.connect("camp.db")

conn.execute("delete from attendance where name='Mahalaxmi'")
print(conn.total_changes)

conn.commit()
conn.close()

