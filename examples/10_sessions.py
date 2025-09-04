from flask import Flask, session
app = Flask(__name__)
app.secret_key = "supersecret"

@app.route("/login/<user>")
def login(user):
    session["user"] = user
    return f"Logged in as {user}"

@app.route("/profile")
def profile():
    return f"Profile of {session.get('user', 'Guest')}"

if __name__ == "__main__":
    app.run()
