from flask import Flask, request, render_template, redirect, session
from models import *

app = Flask(__name__)
app.secret_key = b'Y\xf1Xz\x00\xad|eQ\x80t \xca\x1a\x10K'

@app.route('/', methods=["GET", "POST"], strict_slashes=False)
def home_page():
    users = get_users()
    if session.get('current_user') is None:
        return render_template("login.html", users = users)
    else:
        return render_template("fsa.html", user = session['current_user'])


@app.route('/make_user', methods=["GET", "POST"], strict_slashes=False)
def registration():
    login = request.form.get("login")
    password = request.form.get("password")
    create_user(login, password)
    session['current_user'] = get_user(login)
    return redirect("/")

if __name__ == "__main__":
    app.run("0.0.0.0", 5000)
    