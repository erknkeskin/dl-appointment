from model.appointment import Appointment, AppointmentSchema, db
from datetime import datetime


class AppointmentDao:

    @staticmethod
    def get_appointments():
        try:
            return Appointment.query.order_by(Appointment.appointment_id.desc()).limit(5).all()
        except:
            return False

    @staticmethod
    def delete_appointment(appointment_id):
        try:
            appointment = Appointment.query.filter_by(appointment_id=appointment_id).first()
            db.session.delete(appointment)
            db.session.commit()
            return True
        except:
            return False

    @staticmethod
    def get_appointment(appointment_id):
        try:
            result = Appointment.query.filter_by(appointment_id=appointment_id).first()
            appointment_schema = AppointmentSchema()
            appointment = appointment_schema.dump(result)
            return {
                'data': appointment
            }
        except:
            return {
                'data': None
            }

    @staticmethod
    def change_appointment_status(appointment_id, appointment_status):
        try:
            appointment = Appointment.query.filter_by(appointment_id=appointment_id).first()
            appointment.appointment_modified = datetime.now()
            appointment.appointment_status = appointment_status
            db.session.commit()
            return True
        except:
            return False

    @staticmethod
    def load_more(appointment_id):
        try:
            result = Appointment.query.filter(Appointment.appointment_id < appointment_id).order_by(
                Appointment.appointment_id.desc()).limit(5).all()

            appointment_schema = AppointmentSchema(many=True)
            appointment = appointment_schema.dump(result)

            return {
                'data': appointment
            }
        except:
            return {
                'data': None
            }

    @staticmethod
    def save_appointment(appointment_data):
        try:
            appointment_date_object = datetime.strptime(appointment_data['appointment_date'], '%d/%m/%Y')

            if int(appointment_data['appointment_id']) > 0:
                appointment = Appointment.query.get(int(appointment_data['appointment_id']))
                appointment.appointment_title = appointment_data['appointment_title']
                appointment.appointment_date = appointment_data['appointment_date']
                appointment.appointment_detail = appointment_data['appointment_detail']
                appointment.appointment_modified = datetime.now()
                appointment.appointment_status = 1
                db.session.commit()
                return True
            else:
                appointment = Appointment(
                    appointment_title=appointment_data['appointment_title'],
                    appointment_detail=appointment_data['appointment_detail'],
                    appointment_date=appointment_date_object,
                    appointment_created=datetime.now(),
                    appointment_modified=datetime.now(),
                    appointment_status=1
                )

                db.session.add(appointment)
                db.session.commit()
                return True
        except:
            return False


appointment_dao = AppointmentDao()
