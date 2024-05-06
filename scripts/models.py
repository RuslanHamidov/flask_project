import sqlite3 as sql
from os import path

FULL_PATH = path.join(path.dirname(path.relpath(__file__)), '../database_work/database.db')

class DB_controller:
    def create_user(login, password):
        with sql.connect(FULL_PATH) as con:
            cur = con.cursor()
            cur.execute(f"select id from users where users.logins='{login}'")
            if len(cur.fetchall()) != 0:
                return False
            cur.execute('insert into users (logins, passwords) values(?, ?)', (login, password))
            con.commit()
        return True

    def get_users():
        with sql.connect(FULL_PATH) as con:
            cur = con.cursor()
            cur.execute('select * from users')
            users = cur.fetchall()
        return users

    def get_user(login):
        with sql.connect(FULL_PATH) as con:
            cur = con.cursor()
            cur.execute(f'select * from users where logins="{login}"')
            user = cur.fetchall()
        return user

    def deleteUser(login):
        with sql.connect(FULL_PATH) as con:
            cur = con.cursor()
            cur.execute(f'delete from users where logins="{login}"')
            con.commit()