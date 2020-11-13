"""Sign-up & log-in forms."""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField,IntegerField, HiddenField  
from wtforms.validators import DataRequired, Email, EqualTo, Length, Optional
from wtforms.fields.html5 import DateField


class SignupForm(FlaskForm):
    """User Sign-up Form."""

    name = StringField("Name", validators=[DataRequired()])
    email = StringField(
        "Email",
        validators=[
            Length(min=6),
            Email(message="Enter a valid email."),
            DataRequired(),
        ],
    )
    password = PasswordField(
        "Password",
        validators=[
            DataRequired(),
            Length(min=6, message="Select a stronger password."),
        ],
    )
    confirm = PasswordField(
        "Confirm Your Password",
        validators=[
            DataRequired(),
            EqualTo("password", message="Passwords must match."),
        ],
    )
    passport = StringField("Passport", validators=[Optional()])
    sex = SelectField(u"Sex", choices=[("Male", "Male"), ("FeMale", "FeMale")])
    phone = StringField("Phone Number", validators=[Optional()])
    address = StringField("Address", validators=[Optional()])
    bird = DateField("Date of Bird", validators=[Optional()])
    submit = SubmitField("Register")


class LoginForm(FlaskForm):
    """User Log-in Form."""

    email = StringField(
        "Email", validators=[DataRequired(), Email(message="Enter a valid email.")]
    )
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Log In")

class RequestForm(FlaskForm):
    """Request Form

    Args:
        FlaskForm ([type]): [description]
    """
    type_request = SelectField("Your Request", choices=[("Choose your request", "choice"),("Register New Room", "newroom"), ("Change Room", "changeroom")])

class RoomChoice(FlaskForm):    
    room = IntegerField("New Room", validators=[DataRequired()])
    num_of_domitory = IntegerField("Your Domitory", validators=[DataRequired()])
    num_of_domitory= IntegerField("Your Domitory", validators=[DataRequired()])
    
    submit = SubmitField("Request")
class OtherPointPositioningForm(RoomChoice):
    selected_id = HiddenField()
    newroom = IntegerField("New Room", validators=[DataRequired()])


