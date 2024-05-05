from flask import Flask, request, g, render_template, redirect
from models import *
app = Flask(__name__)


@app.route('/', methods=["GET", "POST"], strict_slashes=False)
def home_page():
    users = get_user()
    if not g.user:
        return render_template("login.html", users = users)
    else:
        return None


@app.route('/make_user', methods=["GET", "POST"], strict_slashes=False)
def registration():
    login = request.form.get("login")
    password = request.form.get("password")
    create_user(login, password)
    return redirect("/")

@app.before_request
def load_user():
    g.user = {}



if __name__ == "__main__":
    app.run("0.0.0.0", 5000)

    