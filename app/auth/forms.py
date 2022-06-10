from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, SubmitField, EmailField, PasswordField
from wtforms.validators import DataRequired, Length



class AuthForm(FlaskForm):
    name = StringField('Name',[DataRequired(), Length(max=50)])
    email = EmailField('Email',[DataRequired(message=('Endereço de e-mail inválido!'))])
    password = PasswordField('Password',[DataRequired(), Length(min=4, message=('Senha deve conter ao menos 4 caracteres.'))])
    recaptcha = RecaptchaField()
    submit = SubmitField('Submit')