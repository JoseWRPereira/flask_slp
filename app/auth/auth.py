from flask import Blueprint, render_template

auth_bp = Blueprint('auth_bp',__name__,
                    template_folder='templates',
                    static_folder='static')

@auth_bp.route('/auth')
def auth():
    return render_template('auth.html')