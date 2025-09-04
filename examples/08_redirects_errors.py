from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return "Home Page"

@app.route("/go-home")
def go_home():
    return redirect(url_for("home"))

@app.errorhandler(404)
def page_not_found(e):
    return render_template("error.html"), 404

if __name__ == "__main__":
    app.run()
