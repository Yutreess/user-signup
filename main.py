from flask import Flask, request, redirect, render_template
import os
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/signup", methods=['GET', 'POST'])
def index():
  return render_template('signup.html')


@app.route("/welcome", methods=['POST'])
def welcome():
  username = request.form['username']
  mismatch = False
  if request.form['pass1'] == request.form['pass2']:
    return render_template("welcome.html", username=username)
  else:
    mismatch = True
    return render_template('signup.html', mismatch=mismatch)

app.run()