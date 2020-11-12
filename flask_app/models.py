"""Database models."""
from . import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
	"""User account model."""

	__tablename__ = 'flasklogin-users'
	id = db.Column(
		db.Integer,
		primary_key=True
	)
	name = db.Column(
		db.String(100),
		nullable=False,
		unique=False
	)
	email = db.Column(
		db.String(40),
		unique=True,
		nullable=False
	)
	password = db.Column(
		db.String(200),
		primary_key=False,
		unique=False,
		nullable=False
	)
	passport = db.Column(db.String(200), nullable=False)
	address= db.Column(db.String(200), nullable=False)
	sex = db.Column(db.String(200), nullable=False)
	dateofbird = db.Column(db.Date(), nullable=False)
	telephone = db.Column(db.Integer, nullable=False)
	numberDomitory = db.Column(db.Integer, nullable=True)
	room = db.Column(db.Integer, nullable=True)
	numofcontract = db.Column(db.Integer, nullable=True)
	startcontract = db.Column(db.Date(), nullable=True)
	endofcontract = db.Column(db.Date(), nullable=True)
	created_on = db.Column(
        db.DateTime,
        index=False,
        unique=False,
        nullable=True
    )
	last_login = db.Column(
        db.DateTime,
        index=False,
        unique=False,
        nullable=True
    )

	def set_password(self, password):
		"""Create hashed password."""
		self.password = generate_password_hash(password, method='sha256')

	def check_password(self, password):
		"""Check hashed password."""
		return check_password_hash(self.password, password)

	def __repr__(self):
		return '<User {}>'.format(self.username)
