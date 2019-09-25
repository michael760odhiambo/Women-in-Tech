from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,PasswordField,BooleanField,SubmitField
from wtforms.validators import Required

class Form(FlaskForm):

    title = StringField(' title',validators=[Required()])
    review = TextAreaField('post review', validators=[Required()])
    submit = SubmitField('Submit')