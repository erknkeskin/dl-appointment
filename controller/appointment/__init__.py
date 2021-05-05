from flask import Blueprint, render_template
from controller.auth import login_required
from service.appointment import appointment_service

bp_appointment = Blueprint('appointment', __name__, url_prefix='/appointment')


@bp_appointment.app_template_filter('date_string_format')
def date_string_format(date_string):
    return date_string.strftime('%d.%m.%Y')


@bp_appointment.app_template_filter('new_appointment_status')
def new_appointment_status(appointment_status):
    if appointment_status == 1:
        return '0'
    else:
        return '1'


@bp_appointment.route('/', methods=['GET'])
@login_required
def site_appointment():
    appointments = appointment_service.get_appointments()
    return render_template('appointment/index.html', datas={'appointments': appointments})


@bp_appointment.route('/delete', methods=['POST'])
@login_required
def delete_appointment():
    return appointment_service.delete_appointment()


@bp_appointment.route('/save', methods=['POST'])
@login_required
def save_appointment():
    return appointment_service.save_appointment()


@bp_appointment.route('/load_more', methods=['POST'])
@login_required
def load_more():
    return appointment_service.load_more()


@bp_appointment.route('/change_status', methods=['POST'])
def change_appointment_status():
    return appointment_service.change_appointment_status()


@bp_appointment.route('/get', methods=['POST'])
@login_required
def get_appointment():
    return appointment_service.get_appointment()
