import sqlite3 as sql
from os import path

ROOT = path.dirname(path.relpath(__file__))

def create_user(login, password):
    con = sql.connect(path.join(ROOT, 'database.db'))
    cur = con.cursor()
    cur.execute('insert into users (logins, passwords) values(?, ?)', (login, password))
    con.commit()
    con.close()

def get_users():
    con = sql.connect(path.join(ROOT, 'database.db'))
    cur = con.cursor()
    cur.execute('select * from users')
    users = cur.fetchall()
    return users

def get_user(login):
    con = sql.connect(path.join(ROOT, 'database.db'))
    cur = con.cursor()
    cur.execute(f'select * from users where logins="{login}"')
    user = cur.fetchall()
    return user