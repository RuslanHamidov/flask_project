from flask import Flask, render_template, session
from scripts.models import DB_controller as db
from scripts.site_login import site_login


app = Flask(__name__,template_folder="static/templates")
app.register_blueprint(site_login)
app.secret_key = b'Y\xf1Xz\x00\xad|eQ\x80t \xca\x1a\x10K'

@app.route('/', methods=["GET", "POST"], strict_slashes=False)
def home_page():
    users = db.get_users()
    if session.get('current_user') is None:
        return render_template("login.html", users = users)
    else:
        return render_template("userpage.html", user = session['current_user'])


if __name__ == "__main__":
    app.run("0.0.0.0", 5000)
    