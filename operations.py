from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import Optional, Required

class Operations(FlaskForm):
	one = IntegerField('Enter Integer 1 ', validators=[Required()])
	two = IntegerField('Enter Integer 2 ', validators=[Required()])
	

	