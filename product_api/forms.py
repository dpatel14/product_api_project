from flask_wtf import FlaskForm
from wtforms import Form,FloatField,IntegerField,SubmitField,StringField,validators
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError

class ProductLogForm(FlaskForm):
	longitude = FloatField('Longitude', validators=[DataRequired()])
	latitude = FloatField('Latitude',  validators=[DataRequired()])
	elevation = IntegerField('Elevation', validators=[DataRequired()])	
	
	submit = SubmitField('Submit')