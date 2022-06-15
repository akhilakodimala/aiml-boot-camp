import sqlite3
conn=sqlite3.connect('camp.db')

res=conn.execute("select *from attendance")
for i in res:
    print(i)