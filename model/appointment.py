from app import db, ma


class Appointment(db.Model):
    __tablename__ = 'appointment'
    __table_args__ = {'extend_existing': True}
    appointment_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    appointment_title = db.Column(db.String, nullable=False)
    appointment_detail = db.Column(db.Text, nullable=True)
    appointment_date = db.Column(db.DateTime, nullable=False)
    appointment_created = db.Column(db.DateTime, nullable=False)
    appointment_modified = db.Column(db.DateTime, nullable=False)
    appointment_status = db.Column(db.Integer, nullable=False, default=0)


class AppointmentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Appointment
