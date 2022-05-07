from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL

class MappingRequestForm(FlaskForm):
    target_url = StringField('URL to be shortened: ', validators=[DataRequired(), URL(message = "Incorrect URL, maybe you forgot to specify protocol (e.g. http://)?")])
    custom_url = StringField('Custom URL: ', validators=[DataRequired()])
    submit = SubmitField('Shorten')
