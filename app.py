from flask import Flask, request, g, render_template

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def home_page():
    return render_template("login.html")


@app.route('/reg', methods=["GET", "POST"], strict_slashes=False)
def registration():
    login = request.form.get("login")
    password = request.form.get("password")


if __name__ == "__main__":
    app.run("0.0.0.0", 5000)