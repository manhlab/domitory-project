"""Logged-in page routes."""
from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user, login_required, logout_user


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
            items=["Request", "Infomation", "Logout"],
        )
    else:
        return render_template("index.jinja2")


@main_bp.route("/about", methods=["GET"])
def about():
    if current_user.is_authenticated:
        return render_template(
            "about.jinja2",
            current_user=current_user,
            items=["Request", "Infomation", "Logout"],
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
            items=["Request", "Infomation", "Logout"],
        )
    else:
        return render_template("index.jinja2")




@main_bp.route("/logout")
@login_required
def logout():
    """User log-out logic."""
    logout_user()
    return redirect(url_for("auth_bp.login"))


@main_bp.route("/publicSpace", methods=["GET"])
def publicSpace():
    if current_user.is_authenticated:
        return render_template(
            "publicSpace.jinja2",
            current_user=current_user,
            items=["Request", "Infomation", "Logout"],
        )
    else:
        return render_template("publicSpace.jinja2")


@main_bp.route("/housing", methods=["GET"])
def housing():
    if current_user.is_authenticated:
        return render_template(
            "housing.jinja2",
            current_user=current_user,
            items=["Request", "Infomation", "Logout"],
        )
    else:
        return render_template("housing.jinja2")


@main_bp.route("/sport", methods=["GET"])
def sport():
    if current_user.is_authenticated:
        return render_template(
            "sport.jinja2",
            current_user=current_user,
            items=["Request", "Infomation", "Logout"],
        )
    else:
        return render_template("sport.jinja2")


@main_bp.route("/livingCost", methods=["GET"])
def livingCost():
    if current_user.is_authenticated:
        return render_template(
            "livingCost.jinja2",
            current_user=current_user,
            items=["Request", "Infomation", "Logout"],
        )
    else:
        return render_template("livingCost.jinja2")
