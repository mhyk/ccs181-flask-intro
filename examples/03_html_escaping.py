from flask import Flask
app = Flask(__name__)

@app.route("/user/<name>")
def user(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    app.run()
