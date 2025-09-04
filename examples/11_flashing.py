from flask import Flask, flash, redirect, url_for, get_flashed_messages
app = Flask(__name__)
app.secret_key = "supersecret"

@app.route("/flash")
def flash_message():
    flash("You were successfully logged in!")
    return redirect(url_for("messages"))

@app.route("/messages")
def messages():
    msgs = get_flashed_messages()
    return "<br>".join(msgs)

if __name__ == "__main__":
    app.run()
