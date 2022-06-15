import sqlite3
conn = sqlite3.connect("camp.db")
conn.execute("drop table attendance")
conn.close()