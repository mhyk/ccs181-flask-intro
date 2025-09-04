from flask import Flask, Response
app = Flask(__name__)

@app.route("/custom-response")
def custom_response():
    return Response("Custom response", status=202, headers={"X-My-Header": "Value"})

if __name__ == "__main__":
    app.run()
