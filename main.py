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
  password = request.form['pass1']
  verified_password = request.form['pass2']
  uname_error = ''
  password_error = ''
  email_error = ''

  # USERNAME CHECKS

  # Check if Username is empty
  if not username:
    uname_error = 'Please enter a Username'

  # Check if username is between 3 and 20 characters 
  elif re.match("^.{3,20}$", username) == None:
    uname_error = 'Username must be between 3 and 20 characters long'

  # Check if username has any spaces
  elif re.search("^\s", username) != None:
    uname_error = 'Username cannot contain spaces'

  # Check if username has special characters
  elif re.match("^[a-zA-Z0-9]{3,20}$", username) == None:
    uname_error = "Username can only contain letters and/or numbers."


  # END USERNAME CHECKS

  # PASSWORD CHECKS

  # Check if any of the password boxes are empty
  if not password or not verified_password:
    password_error = 'Please enter a password and retype it below'
    
  # Check if passwords match
  if password != verified_password:
    password_error = 'Passwrds do not match'

  # Check if either password has spaces
  elif re.search("^\s", password) != None:
    password_error = "Password cannot contain spaces"
  elif re.match("^.{3,20}$", password) == None:
    password_error = "Password must be between 3 and 20 characters"

  # END PASSWORD CHECKS

  # EMAIL CHECKS
  if email:
    if re.match("[a-zA-Z.-_]+@[a-zA-Z-_.]+\.[a-zA-Z0-9]{3,20}", email) == None:
      email_error = "Email must be in the form of \"emailname@host.domain\""
    elif re.search("@@", email) != None or re.search("@+[a-zA-Z-_.]+@", email) != None:
      email_error = "Email can only contain 1 at sign (@)"
  # END EMAIL CHECKS
  
  # Check for previous errors, rerender template if any are present
  if uname_error or password_error or email_error:
    return render_template('signup.html', username=username, email=email,
    email_error=email_error, uname_error=uname_error,
    password_error=password_error)
    
  else:
    return redirect('/welcome?uname={0}'.format(username))

@app.route("/welcome")
def welcome():
  username = request.args.get('uname')
  return render_template('welcome.html', username=username)

app.run()