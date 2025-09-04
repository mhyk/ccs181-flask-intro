from flask import Flask, render_template
app = Flask(__name__)

@app.route("/home")
@app.route("/")
def home():
    return render_template("index.html", user="Chanzed")

@app.route("/about")
def about():
    return render_template("index.html")

@app.route("/profile")
def profile():
    return "Profile Page"


if __name__ == "__main__":
    app.run()
