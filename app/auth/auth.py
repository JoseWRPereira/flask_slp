from flask import Blueprint, redirect, render_template, url_for
from flask import flash
from .forms import AuthForm
from app.db.dbcon import DBConn
from flask import session

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
            db = DBConn()
            u = db.sql_fetch("SELECT id,name,email,password,nif,admin FROM users WHERE email='{}';".format(form.email.data) )
            if u:
                if u[0][3] != str(form.password.data):
                    flash('Senha incorreta!','alert')
                else:
                    session['id']       = u[0][0]
                    session['username'] = u[0][1]
                    session['email']    = u[0][2]
                    session['nif']      = u[0][4]
                    session['admin']    = u[0][5]
                    flash('Usuário autenticado!','alert')
            else:
                flash('Usuário não encontrado/cadastrado!','alert')
            return redirect(url_for('auth_bp.auth'))
    else:
        return render_template('auth.html', form=form )


@auth_bp.route('/auth_success')
def auth_success():
    return "Autenticado com sucesso!"

