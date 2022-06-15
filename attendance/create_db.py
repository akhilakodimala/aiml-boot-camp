import sqlite3
conn=sqlite3.connect('camp.db')

query='''
      create table attendance(g_id int primary key,name text not null,attendance_perc int not null)
     '''
conn.execute((query))