from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Debug mode example"

if __name__ == "__main__":
    app.run()
# Debug mode is controlled by .flaskenv
