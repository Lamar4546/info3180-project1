from flask_wtf import FlaskForm
from wtforms import FloatField, StringField, SubmitField, TextAreaField, FileField, SelectField, IntegerField
from wtforms.validators import DataRequired

class PropertyForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    bedrooms = IntegerField('Bedrooms', validators=[DataRequired()])
    bathrooms = IntegerField('Bathrooms', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    price = FloatField('Price', validators=[DataRequired()])
    type = SelectField('Type', choices=[('House', 'House'), ('Apartment', 'Apartment')], validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    photo = FileField('Photo', validators=[DataRequired()])
    submit = SubmitField('Add Property')