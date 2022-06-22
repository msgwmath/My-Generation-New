# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request, redirect
from model import get_generation
from datetime import datetime


# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
  props = {
    'title': "My Generation", 'first_name': "Susannah"
  }
  return render_template("index.html", time = datetime.now(), props = props)

@app.route('/results', methods = ["GET", "POST"])
def results():
  if request.method == "POST":
    print(request.form["birth year"])
    user_birth_year = request.form["birth year"]
    user_name = request.form["name"]
    generation = get_generation(user_birth_year)
    return render_template("results.html", user_birth_year = user_birth_year, user_name = user_name, generation = generation)
  else:
    return redirect('/')

@app.route("/secret")
def secret():
  return "You found the secret page!"