import sqlite3
conn=sqlite3.connect('camp.db')

str=conn.execute("pragma table_info('attendance')")
print(str)
for i in str:
    print(i)
