from flask import Flask, render_template, request, redirect, url_for, Response, session, flash
import os

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "ccc181-2k25")

@app.route("/")
def home():
    return render_template("index.html", user="Guest")

@app.route("/user/<name>")
def user(name):
    return f"Hello, {name}!"

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/greet", methods=["GET", "POST"])
def greet():
    if request.method == "POST":
        name = request.form["name"]
        return f"Hello, {name}!"
    return '<form method="POST"><input name="name"><input type="submit"></form>'

@app.route("/go-home")
def go_home():
    return redirect(url_for("home"))

@app.errorhandler(404)
def page_not_found(e):
    return render_template("error.html"), 404

@app.route("/custom-response")
def custom_response():
    return Response("Custom response", status=202, headers={"X-My-Header": "Value"})

@app.route("/login/<user>")
def login(user):
    session["user"] = user
    return f"Logged in as {user}"

@app.route("/profile")
def profile():
    user = session.get("user", "Guest")
    return f"Profile of {user}"

@app.route("/flash")
def flash_message():
    flash("You were successfully logged in!")
    return redirect(url_for("messages"))

@app.route("/messages")
def messages():
    from flask import get_flashed_messages
    msgs = get_flashed_messages()
    return "<br>".join(msgs)

@app.route("/log")
def log():
    app.logger.info("Log route was visited")
    return "Logged an event!"

class SimpleMiddleware:
    def __init__(self, app):
        self.app = app
    def __call__(self, environ, start_response):
        print("Request intercepted by middleware")
        return self.app(environ, start_response)

app.wsgi_app = SimpleMiddleware(app.wsgi_app)

if __name__ == "__main__":
    app.run()
