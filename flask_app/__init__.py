"""Initialize app."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_admin import BaseView, expose
import os.path as op
import os
import flask_login

db = SQLAlchemy()
login_manager = LoginManager()

from .models import User, Rooms, RequestsForm

# Customized admin interface
class CustomView(ModelView):
    list_template = 'list.html'
    create_template = 'create.html'
    edit_template = 'edit.html'
    def is_accessible(self):
        return flask_login.current_user.email=='admin'


class StudentsView(ModelView):
    searchable_columns = ('name', 'email', 'room')
    excluded_list_columns = ['password']
    list_columns = ('name', 'email', 'passport', 'address', 'dateofbird', 'telephone','numberDomitory', 'room', 'numofcontract', 'startcontract', 'endofcontract' )
    form_columns = ('name', 'email', 'password', 'passport', 'address', 'dateofbird')
    list_template = 'atendimento/list.html'
    create_template = 'atendimento/create.html'
    edit_template = 'atendimento/edit.html'
    def is_accessible(self):
        return flask_login.current_user.email =='admin'

def create_app():
    """Construct the core app object."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")
    app.config["SQLALCHEMY_BINDS"] = {
        "rooms": "sqlite:///rooms.sqlite",
        "request": "sqlite:///request.sqlite",
    }
    app.config["DATABASE_FILE"] = "students.sqlite"
    app.config["FLASK_ADMIN_SWATCH"] = "flatly"
    app.config["SQLALCHEMY_ECHO"] = True    

    # admin.add_view(MyModelView(User, db.session, category="Menu"))
    # admin.add_view(PostView(RequestsForm, db.session, category="Menu"))
    # Initialize Plugins
    db.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        from . import routes
        from . import auth
        from .assets import compile_static_assets

        # Register Blueprints
        app.register_blueprint(routes.main_bp)
        app.register_blueprint(auth.auth_bp)
        admin = Admin(app, "Admin View", template_mode="bootstrap3", base_template='layout.html')
        admin.add_view(StudentsView(User, db.session))
        admin.add_view(CustomView(RequestsForm, db.session))
        admin.add_view(CustomView(Rooms, db.session))
        # admin.add_view(MyModelView(User, db.session, menu_icon_type='fa', menu_icon_value='fa-server', name="Roles"))
        # admin.add_view(UserView(User, db.session, menu_icon_type='fa', menu_icon_value='fa-users', name="Users"))
        # admin.add_view(CustomView(name="Custom view", endpoint='custom', menu_icon_type='fa', menu_icon_value='fa-connectdevelop',))
        # Create Database Models
        db.create_all()
        app_dir = op.realpath(os.path.dirname(__file__))
        database_path = op.join(app_dir, app.config['DATABASE_FILE'])
        # Compile static assets
        if app.config["FLASK_ENV"] == "development":
            compile_static_assets(app)
        return app

