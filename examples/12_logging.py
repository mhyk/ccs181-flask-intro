from flask import Flask
app = Flask(__name__)

@app.route("/log")
def log():
    app.logger.info("Log route was visited")
    return "Logged an event!"

if __name__ == "__main__":
    app.run()
