from flask import Blueprint, redirect, render_template, url_for
from flask import flash
from .forms import AuthForm, UserNew
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

@auth_bp.route('/user_new', methods=['GET', 'POST'])
def user_new():
    form = UserNew()
    if form.validate_on_submit():
        if form.errors:
            flash(form.errors, 'alert')
            return redirect(url_for('auth_bp.user_new'))
        else:
            if form.password.data != form.password_confirm.data:
                flash("Senhas diferentes!", 'alert')
                return redirect(url_for('auth_bp.user_new'))
            else:
                db = DBConn()

                user_id  = db.sql_fetch("SELECT id FROM users WHERE email='{}';".format(str(form.email.data) ))
                if user_id:
                    flash('Usuário já cadastrado!','alert')
                    return redirect(url_for('auth_bp.user_new'))
                else:
                    db.sql_cmd("INSERT INTO users ( name, email, password, admin) VALUES ('{}','{}','{}',False);".format( form.name.data, form.email.data, form.password.data) )
                    return redirect(url_for('api_bp.api_v1_users'))
    else:
        return render_template('user_new.html', form=form )


@auth_bp.route('/user_list', methods=['GET'])
def user_list():
    db = DBConn()
    lst = db.sql_fetch("SELECT * from users;")
    return "{}".format(lst)
