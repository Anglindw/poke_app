from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo

class PokedexEntry(FlaskForm):
    entry = StringField('Entry', validators=[DataRequired()])
    submit = SubmitField()