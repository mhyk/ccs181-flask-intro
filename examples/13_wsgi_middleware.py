from flask import Flask
app = Flask(__name__)

class SimpleMiddleware:
    def __init__(self, app):
        self.app = app
    def __call__(self, environ, start_response):
        print("Request intercepted by middleware")
        return self.app(environ, start_response)

app.wsgi_app = SimpleMiddleware(app.wsgi_app)

@app.route("/")
def home():
    return "Hello with Middleware!"

if __name__ == "__main__":
    app.run()
