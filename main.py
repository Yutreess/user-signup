from flask import Flask, request, redirect, render_template
import os
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/", methods=['GET', 'POST'])
def index():
  return render_template('signup.html')

app.run()