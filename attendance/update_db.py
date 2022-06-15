import sqlite3
conn=sqlite3.connect('camp.db') #step 2 and step 3

query = '''update attendance set name='Mahalaxmi' where g_id=2216125
        '''

conn.execute(query)

print(conn.total_changes)
conn.commit()
conn.close()