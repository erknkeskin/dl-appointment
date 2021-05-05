from dao.appointment import appointment_dao
from flask import request, jsonify


class AppointmentService:

    def __init__(self):
        self.appointment_id = 0
        self.appointment_title = None
        self.appointment_date = None
        self.appointment_detail = None
        self.appointment_status = None

    def get_all_post_data(self):
        self.appointment_id = request.form.get('appointment_id')
        self.appointment_title = request.form.get('appointment_title')
        self.appointment_date = request.form.get('appointment_date')
        self.appointment_detail = request.form.get('appointment_detail')

    @staticmethod
    def get_appointments():
        return appointment_dao.get_appointments()

    def get_appointment(self):
        self.appointment_id = request.form.get('appointment_id')

        if self.appointment_id == 0:
            return jsonify({'status': 'error', 'message': 'ID gereklidir!'})

        appointment = appointment_dao.get_appointment(self.appointment_id)

        if appointment:
            return jsonify({'status': 'ok', 'data': appointment['data']})
        else:
            return False

    def delete_appointment(self):
        self.appointment_id = request.form.get('appointment_id')

        if self.appointment_id == 0:
            return jsonify({'status': 'error', 'message': 'ID gereklidir!'})

        appointment = appointment_dao.delete_appointment(self.appointment_id)

        if appointment:
            return jsonify({'status': 'ok', 'message': 'Randevu silindi'})
        else:
            return jsonify({'status': 'error', 'message': 'Randevu silinemedi'})

    def change_appointment_status(self):
        self.appointment_id = request.form.get('appointment_id')
        self.appointment_status = request.form.get('appointment_status')

        if self.appointment_id == 0:
            return jsonify({'status': 'error', 'message': 'ID gereklidir!'})

        if self.appointment_status is None:
            return jsonify({'status': 'error', 'message': 'Status gereklidir!'})

        result = appointment_dao.change_appointment_status(self.appointment_id, self.appointment_status)

        if result:
            return jsonify({'status': 'ok'})
        else:
            return jsonify({'status': 'error'})

    def load_more(self):
        self.appointment_id = request.form.get('last_id')

        if self.appointment_id == 0:
            return jsonify({'status': 'error'})

        result = appointment_dao.load_more(self.appointment_id)

        if result:
            return jsonify({'status': 'ok', 'data': result['data']})
        else:
            return jsonify({'status': 'error'})

    def save_appointment(self):

        self.get_all_post_data()

        if self.appointment_title is None:
            return jsonify({'status': 'error', 'message': 'Randevu başlığı gereklidir!'})

        if self.appointment_date is None:
            return jsonify({'status': 'error', 'message': 'Randevu tarihi gereklidir!'})

        appointment_data = {
            'appointment_id': self.appointment_id,
            'appointment_title': self.appointment_title,
            'appointment_date': self.appointment_date,
            'appointment_detail': self.appointment_detail,
        }

        result = appointment_dao.save_appointment(appointment_data)

        if result:
            return jsonify({'status': 'ok', 'message': 'kaydedildi!'})
        else:
            return jsonify({'status': 'error', 'message': 'kaydedilemedi!'})


appointment_service = AppointmentService()
