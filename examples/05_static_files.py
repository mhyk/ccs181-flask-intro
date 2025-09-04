from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>hello world</h1>"
    #return render_template("index.html", user="Static Demo")

if __name__ == "__main__":
    app.run()
