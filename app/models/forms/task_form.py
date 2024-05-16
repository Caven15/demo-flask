from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length

class TaskForm(FlaskForm):
    nom = StringField('Nom', validators=[DataRequired()])
    description = StringField('Description',validators=[DataRequired(), Length(max=200)])