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
  email_error = ''
  password_error = ''
  verify_password_error = ''
  
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

  # Check if password is empty
  if not password:
    password_error = 'Please enter a password and retype it below'
  # Check if password has spaces
  elif re.search("^\s", password) != None:
    password_error = "Password cannot contain spaces"
  # Check if password is in the character range
  elif re.match("^.{3,20}$", password) == None:
    password_error = "Password must be between 3 and 20 characters"

  # Check if verified password is empty
  if not verified_password:
    verify_password_error = 'Remember to retype the password from above'
    """
    # Empty verify_password_error if it's the same as the password error
    if verify_password_error == password_error:
      verify_password_error = ''
    """
  # Check if verified password has spaces
  elif re.search("^\s", verified_password) != None:
    verify_password_error = "Password cannot contain spaces"
    """
    # Empty verify_password_error if it's the same as the password error
    if verify_password_error == password_error:
      verify_password_error = ''
    """
  # Check if verified password is in the character range
  elif re.match("^.{3,20}$", verified_password) == None:
    verify_password_error = "Password must be between 3 and 20 characters"
    """
    # Empty verify_password_error if it's the same as the password error
    if verify_password_error == password_error:
      verify_password_error = ''
    """

  # Check if passwords match
  if password != verified_password:
    verify_password_error = ''
    password_error = 'Passwords do not match'

  # END PASSWORD CHECKS

  # EMAIL CHECKS
  if email:
    if re.search("@", email) == None:
      email_error = "Email must contain an at sign '@'"
    elif re.search("\.", email) == None:
      email_error = "Email must contain a dot '.'"
    elif re.match("^.+\.$", email) != None:
      email_error = "Email cannot end in a dot '.'"
    elif re.search("@@", email) != None or re.search("@+[a-zA-Z-_.]+@", email) != None:
      email_error = "Email can only contain 1 at sign '@'"
    elif re.match("^.+@$", email) != None:
      email_error = "Email cannot end in an at sign '@'"
    elif re.match("[a-zA-Z.-_]+@[a-zA-Z-_.]+\.[a-zA-Z0-9]{3,20}", email) == None:
      email_error = "Email must be in the form of \"emailname@host.domain\""
  # END EMAIL CHECKS
  
  # Check for previous errors, rerender template if any are present
  if uname_error or password_error or email_error or verify_password_error:
    return render_template('signup.html', username=username, email=email,
    email_error=email_error, uname_error=uname_error,
    password_error=password_error, verify_password_error=verify_password_error)
    
  else:
    return redirect('/welcome?uname={0}'.format(username))

@app.route("/welcome")
def welcome():
  username = request.args.get('uname')
  return render_template('welcome.html', username=username)

app.run()