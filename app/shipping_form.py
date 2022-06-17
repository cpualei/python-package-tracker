from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from map.map import map

choices = [""]
# choices.extend([city for city in map.keys()])
choices.extend(list(map.keys()))

class ShippingForm(FlaskForm):
    sender = StringField("Sender name", validators=[DataRequired()])
    recipient = StringField("Recipient name", validators=[DataRequired()])
    origin = SelectField("Package origin", choices=choices,
        validators=[DataRequired()])
    destination = SelectField("Package destination", choices=choices,
        validators=[DataRequired()])
    express = BooleanField("Express")
    submit = SubmitField("Submit")
