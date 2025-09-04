from flask import Flask, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.secret_key = "supersecret"

class NameForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    submit = SubmitField("Submit")

@app.route("/", methods=["GET", "POST"])
def form():
    form = NameForm()
    if form.validate_on_submit():
        flash(f"Hello {form.name.data}!")
        return redirect(url_for("messages"))
    return render_template("form.html", form=form)

@app.route("/messages")
def messages():
    from flask import get_flashed_messages
    msgs = get_flashed_messages()
    return "<br>".join(msgs)

if __name__ == "__main__":
    app.run()
