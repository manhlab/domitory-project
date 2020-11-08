from flask import Flask, flash, render_template, request, redirect, url_for, send_from_directory
from flask_cors import CORS
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


# SQL part
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite'
app.config['SECRET_KEY'] = "random string"
CORS(app)

db = SQLAlchemy(app)


class Student(db.Model):
    __tablename__ = 'student'
    id = db.Column('student_id', db.Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    passport = Column(String(250), nullable=False)
    date = Column(String(250), nullable=False)
    request = Column(String(250), nullable=False)
    room = Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.name


def __init__(self, name, passport, date, request, room):
    self.name = name
    self.passport = passport
    self.date = date
    self.request = request
    self.room = room


db.create_all()
# Flask part
ENTRY_POINT = '/'


@app.route(ENTRY_POINT, methods=['GET', 'POST'])
def new():
    if request.method == 'GET':
        return render_template('request.html')

    if request.method == 'POST':
        print(request.form)
        student_form = Student(name=request.form['name'], passport=request.form['passport'],
                        date=request.form['email'], request=request.form['request'],
                        room=request.form['currentroom']
                        )
        db.session.add(student_form)
        db.session.commit()
        flash('Record was successfully added')
        return render_template('success.html')


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
    return render_template("result.html", result=result)

# @app.route("/query", methods=['GET'])
# def query():
#   return render_template("success.html")
