from flask import Blueprint, redirect, render_template, url_for
from flask import flash
from .forms import AuthForm

auth_bp = Blueprint('auth_bp',__name__,
                    template_folder='templates',
                    static_folder='static')


@auth_bp.route('/auth', methods=['GET', 'POST'])
def auth():
    form = AuthForm()
    if form.validate_on_submit():
        if form.errors:
            flash(form.errors, 'alert')
            return redirect(url_for('auth_bp.auth'))
        else:
            return redirect(url_for('auth_bp.auth_success'))
    else:
        return render_template('auth.html', form=form )


@auth_bp.route('/auth_success')
def auth_success():
    return "Autenticado com sucesso!"

