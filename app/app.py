from flask import (
    Flask,
    flash,
    render_template,
    request,
    redirect,
    url_for,
    send_from_directory,
)
from flask_cors import CORS
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, ForeignKey, Integer, String, Date, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from utils import time_format, hash_format
import os
import sys

# SQL part
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///students.sqlite"
app.config["SECRET_KEY"] = "random string"
CORS(app)
db = SQLAlchemy(app)





class Student(db.Model):
    __tablename__ = "student"
    id = db.Column("student_id", db.Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    passport = Column(String(250), nullable=False)
    sex = Column(String(250), nullable=False)
    dateofbird = Column(Date(), nullable=False)
    telephone = Column(db.Integer, nullable=False)
    room = Column(db.Integer, nullable=False)
    numofcontract = Column(db.Integer, nullable=False)
    startcontract = Column(Date(), nullable=False)
    endofcontract = Column(Date(), nullable=False)
    passwd = Column(String(250), nullable=False)

    def __repr__(self):
        return "<User %r>" % self.name


def __init__(
    self,
    name,
    email,
    passport,
    sex,
    dateofbird,
    telephone,
    room,
    numofcontract,
    startcontract,
    endofcontract,
    passwd,
):
    self.name = name
    self.email = email
    self.passport = passport
    self.sex = sex
    self.dateofbird = dateofbird
    self.telephone = telephone
    self.room = room
    self.numofcontract = numofcontract
    self.startcontract = startcontract
    self.endofcontract = endofcontract
    self.passwd = passport


db.create_all()

# Flask part
@app.route("/", methods=["GET", "POST"])
def request_form():
    return render_template("index.html")


@app.route("/auth", methods=["POST", "GET"])
def auth():
    if request.method == "GET":
        return render_template("auth.html")


@app.route("/request", methods=["GET", "POST"])
def form():
    if request.method == "GET":
        return render_template("request.html")

    if request.method == "POST":
        student_form = Student(
            name=request.form["name"],
            email=request.form["email"],
            passport=request.form["passport"],
            sex=request.form["sex"],
            dateofbird=time_format(request.form["dateoftract"]),
            telephone=request.form["telephone"],
            room=request.form["room"],
            numofcontract=request.form["numofcontract"],
            startcontract=time_format(request.form["dateofstart"]),
            endofcontract=time_format(request.form["dateofend"]),
            passwd=request.form["passwd"],
        )
        db.session.add(student_form)
        db.session.commit()
        flash("Record was successfully added")
        return render_template("success.html")


@app.route("/about", methods=["GET"])
def about():
    return render_template("about.html")


@app.route("/signin", methods=["GET", "POST"])
def signin():
    if request.method == "GET":
        return render_template("signin.html")

    if request.method == "POST":
        student_form = Student(
            name=request.form["name"],
            email=request.form["email"],
            passport=request.form["passport"],
            sex=request.form["sex"],
            dateofbird=time_format(request.form["dateofbird"]),
            telephone=request.form["phone"],
            room=request.form["room"],
            numofcontract=request.form["numofcontract"],
            startcontract=time_format(request.form["dateofstart"]),
            endofcontract=time_format(request.form["dateofend"]),
            passwd=hash_format(request.form["passwd"]),
        )
        db.session.add(student_form)
        db.session.commit()
        return render_template("success.html")
@app.route("/publicSpace", methods=["GET"])
def publicSpace():
    if request.method == "GET":
        return render_template("publicSpace.html")
@app.route("/housing", methods=["GET"])
def housing():
    if request.method == "GET":
        return render_template("housing.html")
@app.route("/sport", methods=["GET"])
def sport():
    if request.method == "GET":
        return render_template("sport.html")
@app.route("/livingCost", methods=["GET"])
def livingCost():
    if request.method == "GET":
        return render_template("livingCost.html")