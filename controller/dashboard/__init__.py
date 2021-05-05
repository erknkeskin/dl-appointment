from flask import Blueprint, render_template
from controller.auth import login_required

bp_dashboard = Blueprint('dashboard', __name__)

@bp_dashboard.route('/', methods=['GET'])
@login_required
def site_dashboard():
    return render_template('dashboard/index.html')