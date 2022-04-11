from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class FlashcardForm(FlaskForm):
  collection = StringField('Collection', validators=[DataRequired()])
  front = StringField('Front', validators=[DataRequired()])
  back = StringField('Back', validators=[DataRequired()])
  submit = SubmitField('Add Flashcard')