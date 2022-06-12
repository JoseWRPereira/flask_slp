from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, PasswordField
from wtforms.validators import DataRequired, Length

class AuthForm(FlaskForm):
    email = EmailField( 'E-mail',
                        [   DataRequired(
                            message=('Endereço de e-mail inválido!'))
                        ])
    password = PasswordField('Senha',
                        [   DataRequired(), 
                            Length(min=4, 
                                message=('Senha deve conter ao menos 4 caracteres.'))
                        ])
    submit = SubmitField('Enviar')

class UserNew(FlaskForm):
    name = StringField('Nome', [DataRequired()])
    email = EmailField("E-mail", [DataRequired()])
    password = PasswordField("Senha", [DataRequired(),Length(min=4,message=('Senha deve conter ao menos 4 caracteres.'))])
    password_confirm = PasswordField("Confirmar Senha", [DataRequired(),Length(min=4,message=('Senha deve conter ao menos 4 caracteres.'))])
    submit = SubmitField('Salvar')
