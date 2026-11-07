
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("signup.html")


@app.route("/signup", methods=["POST"])
def signup():
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    password = request.form.get("password", "").strip()

    if not name or not email or not password:
        return "Error: Please fill in all three fields.", 400

    return redirect(url_for("welcome", name=name))


@app.route("/welcome/<name>")
def welcome(name):
    return render_template("welcome.html", name=name)


@app.route("/search", methods=["GET"])
def search():
    term = request.args.get("term", "").strip()
    return render_template("search.html", term=term)


if __name__ == "__main__":
    app.run(debug=True)


