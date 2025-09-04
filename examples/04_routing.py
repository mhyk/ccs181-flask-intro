from flask import Flask
app = Flask(__name__)


@app.route("/")
def index():
    return "This is the homepage."


@app.route("/hello")
def hello():
    return "Hello, Flask!"


@app.route("/user/<username>")
def show_user(username):
    return f"Hello, {username}!"


@app.route("/post/<int:post_id>")
def show_post(post_id):
    return f"Post number {post_id}"


if __name__ == "__main__":
    app.run()
