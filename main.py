from flask import Flask, request, redirect, render_template
import os
import cgi
import re

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/signup")
def index():
  return render_template('signup.html')


@app.route("/signup", methods=['POST'])
def validate():
  username = request.form['username']
  email = request.form['email']
  uname_error = ''
  password_empty = ''
  password_mismatch = ''

  # Check if Username is empty
  if not username:
    uname_error = 'Please enter a Username'
  elif ' ' in username:
    uname_error = 'Username cannot contain spaces'
  elif len(username) < 3 or len(username) > 20:
    uname_error = 'Username must be between 3 and 20 characters long'


  # Check if passwords are empty
  if not request.form['pass1']:
    password_empty = 'Please enter a password and retype it below'
    
  # Check if passwords match
  if not (request.form['pass1'] == request.form['pass2']):
    password_mismatch = 'Passwrds do not match'
  
  # Check for previous errors, rerender template if any are present
  if uname_error or password_empty or password_mismatch:
    return render_template('signup.html', username=username, email=email,
    uname_empty=uname_error,
    password_empty=password_empty, password_mismatch=password_mismatch)
    
  else:
    return redirect('/welcome?uname={0}'.format(username))

@app.route("/welcome")
def welcome():
  username = request.args.get('uname')
  return render_template('welcome.html', username=username)

app.run()