"""Database models."""
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

class User(UserMixin, db.Model):
    """User account model."""

    __tablename__ = "flasklogin-users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=False)
    email = db.Column(db.String(40), unique=True, nullable=False)
    password = db.Column(
        db.String(200), primary_key=False, unique=False, nullable=False
    )
    passport = db.Column(db.String(200), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    sex = db.Column(db.String(200), nullable=False)
    dateofbird = db.Column(db.Date(), nullable=False)
    telephone = db.Column(db.Integer, nullable=False)
    numberDomitory = db.Column(db.Integer, nullable=True)
    room = db.Column(db.Integer, nullable=True)
    numofcontract = db.Column(db.Integer, nullable=True)
    startcontract = db.Column(db.Date(), nullable=True)
    endofcontract = db.Column(db.Date(), nullable=True)
    created_on = db.Column(db.DateTime, index=False, unique=False, nullable=True)
    last_login = db.Column(db.DateTime, index=False, unique=False, nullable=True)

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method="sha256")

    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

    def __repr__(self):
        return "<User {}>".format(self.name)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    # Required for administrative interface
    def __unicode__(self):
        return self.name


class Rooms(UserMixin, db.Model):
    __tablename__ = "rooms"
    __bind_key__ = "rooms"
    id = db.Column("room_id", db.Integer, primary_key=True)
    room = db.Column(db.Integer, nullable=False)
    numberDomitory = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(40), nullable=False)
    number_person = db.Column(db.Integer, nullable=False)
    type_room = db.Column(db.String(250), nullable=False)
    price_room = db.Column(db.Integer, nullable=False)
    empty_position = db.Column(db.String(250), nullable=False)
    status_room = db.Column(db.String(250), nullable=False)
    info = {"bind_key": "rooms"}

    def __repr__(self):
        return "<Room %r>" % self.room
    def __unicode__(self):
        return self.room


class RequestsForm(UserMixin, db.Model):
    __tablename__ = "request"
    __bind_key__ = "request"
    id = db.Column("request_id", db.Integer, primary_key=True)
    email = db.Column(db.String(40), nullable=False)
    request_type = db.Column(db.String(250), nullable=False)
    request_mess = db.Column(db.String(250), nullable=True)
    status_request = db.Column(db.String(250), nullable=True)
    info = {"bind_key": "request"}

    def __repr__(self):
        return "<Request %r>" % self.email
    def __unicode__(self):
        return self.email
