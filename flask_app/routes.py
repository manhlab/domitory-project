"""Logged-in page routes."""
from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import current_user, login_required, logout_user
from .forms import RequestForm
from .models import db, User, Rooms, RequestsForm
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
        messenger_err = []
        request_params = []
        request_params.append(current_user.email)
        request_params.append(request.form['comment'])
        if request.form["sellect"] == "yes":
            request_params.append('change room')
            if  current_user.numberDomitory  == '':
                messenger_err.append("You are not have room!")
                messenger_err.append("Please add new contract!")
            if current_user.room == request.form["nextroom"]:
                messenger_err += ["Next room should diffirence current room!"]
            current_user.room = request.form["nextroom"]
        else:
            request_params.append('new contract')
            if request.form["numberdom"] not in range(1, 5):
                messenger_err.append("Number domitory should in 1-4")
            if request.form["nextroom"] in Rooms.query.filter_by(email=request.form["numberdom"]).select('room'):
                current_user.room = request.form["nextroom"]

            current_user.numberDomitory = request.form["numberdom"]
            current_user.numofcontract = "ITMO-0{}-{}-{}".format(
                request.form["numberdom"], request.form["nextroom"], current_user.id
            )
            current_user.startcontract = datetime.date.today()
            current_user.endofcontract = datetime.date(int(2020), int(6), int(30))

        
        if messenger_err:
            request_params.append("FALSE")
            new_request = RequestsForm(email=request_params[0],
                                request_type= request_params[2],
                                request_mess = request_params[1],
                                status_request= request_params[3],
                                )
            db.session.add(new_request)
            db.session.commit()        
            return render_template(
                "request.jinja2",
                current_user=current_user,
                items=["Request", "Information", "Logout"],
                error=messenger_err,
            )
        else:
            request_params.append("TRUE")
            db.session.commit()
            return render_template(
                "success.jinja2",
                current_user=current_user,
                items=["Request", "Information", "Logout"],
                error=messenger_err,
            )
    return render_template(
        "request.jinja2",
        current_user=current_user,
        items=["Request", "Information", "Logout"],
    )


@main_bp.route("/information", methods=["GET"])
def info():
    if current_user.is_authenticated:
        photolink = (
            "../static/img/boy.png"
            if current_user.sex == "Male"
            else "../static/img/girl.png"
        )
        act = RequestsForm.query.filter_by(email=current_user.email).all()
        print(act)
        return render_template(
            "information.jinja2",
            current_user=current_user,
            items=["Request", "Information", "Logout"],
            username=current_user.name,
            address_user=current_user.address,
            passport_user=current_user.passport,
            numcontract=current_user.numofcontract,
            startcontract=current_user.startcontract,
            endcontract=current_user.endofcontract,
            photo_link=photolink,
            activity=act
        )
    else:
        return render_template("index.jinja2")


@main_bp.route("/admin", methods=["GET"])
def adminview():
    return render_template("adminview.jinja2")
