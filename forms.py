from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, URL, Optional


class Petform(FlaskForm):
    """ Form for adding Pets"""
    Pet_name = StringField('Pet Name', validators=[DataRequired()])
    Species = StringField('Species', validators = [DataRequired()])
    Photo_URL = StringField('Photo URL', validators = [DataRequired()])
    Age = IntegerField('Age', validators = [Optional()])
    Notes = TextAreaField('Notes', validators = [Optional])
    Available = BooleanField('Available for Adoption', default = True)