"""Logged-in page routes."""
from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import current_user, login_required, logout_user
from .forms import RequestForm
from .models import db, User
import datetime

# Blueprint Configuration
main_bp = Blueprint(
    "main_bp", __name__, template_folder="templates", static_folder="static"
)


@main_bp.route("/home", methods=["GET"])
def index():
    if current_user.is_authenticated:
        return render_template(
            "index.jinja2",
            current_user=current_user,
            items=["Request", "Information", "Logout"],
        )
    else:
        return render_template("index.jinja2")


@main_bp.route("/about", methods=["GET"])
def about():
    if current_user.is_authenticated:
        return render_template(
            "about.jinja2",
            current_user=current_user,
            items=["Request", "Information", "Logout"],
        )

    else:
        return render_template("about.jinja2")


@main_bp.route("/", methods=["GET"])
def dashboard():
    """Logged-in User Dashboard."""
    if current_user.is_authenticated:
        return render_template(
            "index.jinja2",
            current_user=current_user,
            items=["Request", "Information", "Logout"],
        )
    else:
        return render_template("index.jinja2")


@main_bp.route("/logout")
@login_required
def logout():
    """User log-out logic."""
    current_user.last_login = datetime.datetime.now()
    db.session.commit()
    logout_user()
    return redirect(url_for("auth_bp.login"))


@main_bp.route("/publicSpace", methods=["GET"])
def publicSpace():
    if current_user.is_authenticated:
        return render_template(
            "publicSpace.jinja2",
            current_user=current_user,
            items=["Request", "Information", "Logout"],
        )
    else:
        return render_template("publicSpace.jinja2")


@main_bp.route("/housing", methods=["GET"])
def housing():
    if current_user.is_authenticated:
        return render_template(
            "housing.jinja2",
            current_user=current_user,
            items=["Request", "Information", "Logout"],
        )
    else:
        return render_template("housing.jinja2")


@main_bp.route("/sport", methods=["GET"])
def sport():
    if current_user.is_authenticated:
        return render_template(
            "sport.jinja2",
            current_user=current_user,
            items=["Request", "Information", "Logout"],
        )
    else:
        return render_template("sport.jinja2")


@main_bp.route("/livingCost", methods=["GET"])
def livingCost():
    if current_user.is_authenticated:
        return render_template(
            "livingCost.jinja2",
            current_user=current_user,
            items=["Request", "Information", "Logout"],
        )
    else:
        return render_template("livingCost.jinja2")


@main_bp.route("/request", methods=["GET", "POST"])
def request_user():
    """
    User sign-up page.

    GET requests serve sign-up page.
    POST requests validate form & user creation.
    """
    if not current_user.is_authenticated:
        flash("You are not login!!")
        return redirect(url_for("main_bp.dashboard"))
    if current_user.is_authenticated and request.method == "POST":
        # ImmutableMultiDict([('currrom', ''), ('nextroom', '123'), ('numberdom', '2'), ('comment', '123123')])
        messenger_err = []

        if request.form['sellect'] == '':
            messenger_err.append("Please sellect sevirce!")

        elif request.form['sellect'] == 'yes':
            if int('0' + current_user.numberDomitory) == 0:
                messenger_err.append("You are not have room!")
                messenger_err.append("Please add new contract!")
            if current_user.room == request.form['nextroom']:
                messenger_err += "Next room should diffirence current room!"
            current_user.room = request.form['nextroom']
        else:
            if int('0' + request.form['numberdom']) not in range(1, 5):
                messenger_err.append("Number domitory should in 1-4")
            current_user.room = request.form['nextroom']
            current_user.numberDomitory = request.form['numberdom']
            current_user.numofcontract = "ITMO-0{}-{}-{}".format(
                request.form['numberdom'], request.form['nextroom'], current_user.id)
            current_user.startcontract = datetime.date.today()
            current_user.endofcontract = datetime.date(
                int(2020), int(6), int(30))

        db.session.commit()
        if messenger_err:
            return render_template(
                "request.jinja2",
                current_user=current_user,
                items=["Request", "Information", "Logout"],
                error=messenger_err
            )
        else:
            return render_template(
                "success.jinja2",
                current_user=current_user,
                items=["Request", "Information", "Logout"],
                error=messenger_err
            )
    return render_template(
        "request.jinja2",
        current_user=current_user,
        items=["Request", "Information", "Logout"],
    )


@main_bp.route("/information", methods=["GET"])
def info():
    if current_user.is_authenticated:
        photolink = "../static/img/boy.png" if current_user.sex=="Male" else "../static/img/girl.png"
        return render_template(
            "information.jinja2",
            current_user=current_user,
            items=["Request", "Information", "Logout"],
            username=current_user.name,
            address_user=current_user.address,
            passport_user=current_user.passport,
            numcontract=current_user.numofcontract,
            strartcontract=current_user.startcontract,
            endcontract=current_user.endofcontract,
            photo_link=photolink
        )
    else:
        return render_template("index.jinja2")
