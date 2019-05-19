from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms.validators import Required

class Operations(FlaskForm):
	one = IntegerField('Enter Integer 1 ', validators=[Required()])
	two = IntegerField('Enter Integer 2 ', validators=[Required()])