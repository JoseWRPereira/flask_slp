from flask import Blueprint, redirect, render_template, url_for

from .forms import AuthForm

auth_bp = Blueprint('auth_bp',__name__,
                    template_folder='templates',
                    static_folder='static')


@auth_bp.route('/auth', methods=['GET','POST'])
def auth():
    form = AuthForm()
    if form.validate_on_submit():
        return redirect(url_for("auth_success"))
    else:
        return render_template('auth.html', form=form, template='form-template')


@auth_bp.route('/auth_success')
def auth_success():
    return "Autenticado com sucesso!"

