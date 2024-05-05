import sqlite3 as sql
from os import path

ROOT = path.dirname(path.relpath(__file__))

def create_user(login, password):
    con = sql.connect(path.join(ROOT, 'database.db'))
    cur = con.cursor()
    cur.execute('insert into posts (login, password) values(?, ?)', (login, password))
    con.commit()
    con.close()
