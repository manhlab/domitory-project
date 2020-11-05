from flask import Flask, flash, render_template, request, redirect, url_for, send_from_directory
from flask_cors import CORS
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
from db_setup import init_db

import os
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydata.db@localhost/admin'
app.secret_key = "secert_key"
db = SQLAlchemy(app)
CORS(app)
init_db()

# Rename this.
ENTRY_POINT = '/'

# And this.
SERVER_ROOT = os.path.dirname(os.getcwd()) + '/MyApp/app'


@app.route(ENTRY_POINT, methods=['GET'])
def index():
    return render_template('contact.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
  if request.method == 'POST':
    result = request.form
  return render_template("result.html",result = result)

@app.route("/query", methods=['GET'])
def query():
    return render_template('success.html')
