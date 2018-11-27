from flask import Flask, request, make_response, redirect, render_template
from datetime import datetime
from flask_moment import Moment

app = Flask(__name__)
moment = Moment(app)


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


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"), 500


if __name__ == '__main__':
    app.run(debug=True)
