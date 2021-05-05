from flask import Blueprint, render_template, redirect, url_for, request
from functools import wraps
from service.auth import *

bp_auth = Blueprint('auth', __name__, url_prefix='/auth')


def login_required(f):
    @wraps(f)
    def is_access(*args, **kwargs):
        if not auth_service.is_logged():
            return redirect(url_for('auth.login'))
        else:
            return f(*args, **kwargs)

    return is_access

@bp_auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return auth_service.login()

    return render_template('auth/login.html')

@bp_auth.route('/logout', methods=['GET'])
def logout():
    auth_service.logout()
    return redirect(url_for('dashboard.site_dashboard'))