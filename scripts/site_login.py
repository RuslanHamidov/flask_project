from flask import request, session, redirect, Blueprint
from scripts.models import DB_controller as db


site_login = Blueprint('site_login', __name__)

@site_login.route('/make_user', methods=["GET", "POST"], strict_slashes=False)
def registration():
    login = request.form.get("login")
    password = request.form.get("password")
    if db.create_user(login, password):
        session['current_user'] = db.get_user(login)
    return redirect("/")

@site_login.route('/logout')
def logout():
    session['current_user'] = None
    return redirect('/')

@site_login.route('/delete_user')
def delete_user():
    db.deleteUser(session['current_user'][0][1])
    session['current_user'] = None
    return redirect('/')
