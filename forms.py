from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, URL, Optional, ValidationError



def validate_species(form, field):
    allowed_species = ["cat", "dog", "porcupine"]
    if field.data.lower()not in allowed_species:
        raise ValidationError("Species must be 'cat , 'dog', or 'porcupine'.")

def validate_age(form, field):
    if field.data  is not None (field.data < 0 or field.data > 30):
        raise ValidationError("Age most between 0 and 30.")

class Petform(FlaskForm):
    """ Form for adding Pets"""
    Pet_name = StringField('Pet Name', validators=[DataRequired()])
    Species = StringField('Species', validators = [DataRequired()])
    Photo_URL = StringField('Photo URL', validators = [DataRequired()])
    Age = IntegerField('Age', validators = [Optional()])
    Notes = TextAreaField('Notes', validators = [Optional])
    Available = BooleanField('Available for Adoption', default = True)


class EditPetForm(FlaskForm):
    photo_url = StringField('Photo URL', validators = [URL()])
    notes = TextAreaField('Notes')
    available = BooleanField('Available For Adoption')