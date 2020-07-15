# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
import model


# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/results', methods = ["GET", "POST"])
def results():
    if request.method == "POST":
        user_birthmonth = request.form["birthmonth"]
        birthstone = model.get_birthstone(user_birthmonth)
        return render_template('results.html', user_birthmonth = user_birthmonth, birthstone = birthstone)
    else:
        return "Error"