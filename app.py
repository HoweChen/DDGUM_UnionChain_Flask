from flask import Flask, request, make_response, redirect, render_template, session
from datetime import datetime
from flask_moment import Moment

# form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config["SECRET_KEY"] = "this is a secret key"
moment = Moment(app)


# create new From
class NameForm(FlaskForm):
    name = StringField("What is your name?", validators=[DataRequired()])
    submit = SubmitField("Submit")


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route("/user/<name>")
def user(name):
    return render_template("user.html", name=name)


@app.route('/useragent')
def useragent():
    user_agent = request.headers.get("User-Agent")
    response = make_response(user_agent)
    response.status_code = 404
    # return f"{user_agent}"
    return response


@app.route('/time')
def time():
    return render_template("time.html", current_time=datetime.utcnow())


@app.route('/baidu')
def baidu():
    return redirect("https://www.baidu.com")


@app.route('/newuser', methods=["GET", "POST"])
def new_user():
    name_form = NameForm()
    if name_form.validate_on_submit():
        session["name"] = name_form.name.data
        return redirect("./success")
    return render_template("new_user.html", form=name_form)


@app.route('/success')
def success():
    return render_template("success.html")


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"), 500


if __name__ == '__main__':
    app.run(debug=True)
