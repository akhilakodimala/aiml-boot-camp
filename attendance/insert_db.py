import sqlite3
conn=sqlite3.connect('camp.db')

conn.execute("insert into attendance values(2216128,'Akhila Kodimala',100)")
conn.execute("insert into attendance values(2216127,'Harini Anenka',100)")
conn.execute("insert into attendance values(2216125,'Mahalaxmi Koleti',100)")

conn.commit()
conn.close()