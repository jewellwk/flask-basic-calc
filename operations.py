from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms.validators import DataRequired

class Operations(FlaskForm):
	one = IntegerField('Enter Integer 1 ', validators=[DataRequired()])
	two = IntegerField('Enter Integer 2 ', validators=[DataRequired()])