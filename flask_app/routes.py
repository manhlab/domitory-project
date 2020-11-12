"""Logged-in page routes."""
from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user, login_required, logout_user


# Blueprint Configuration
main_bp = Blueprint(
    "main_bp", __name__, template_folder="templates", static_folder="static"
)

@main_bp.route("/home", methods=["GET"])
def index():
    return render_template("index.jinja2", current_user=current_user)
@main_bp.route("/about", methods=["GET"])
def about():
    return render_template("about.jinja2")

@main_bp.route("/", methods=["GET"])
@login_required
def dashboard():
    """Logged-in User Dashboard."""
    return render_template(
        "index.jinja2",
        title="Flask-Login Tutorial.",
        template="dashboard-template",
        current_user=current_user,
        items=["Request", "Infomation", "Logout"],
        body="You are now logged in!",
    )


@main_bp.route("/logout")
@login_required
def logout():
    """User log-out logic."""
    logout_user()
    return redirect(url_for("auth_bp.login"))

@main_bp.route("/publicSpace", methods=["GET"])
def publicSpace():
    return render_template("publicSpace.jinja2")
@main_bp.route("/housing", methods=["GET"])
def housing():
    return render_template("housing.jinja2")
@main_bp.route("/sport", methods=["GET"])
def sport():
    return render_template("sport.jinja2")
@main_bp.route("/livingCost", methods=["GET"])
def livingCost():
    return render_template("livingCost.jinja2")
