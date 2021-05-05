import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://erkan:123@localhost/appointmentdb1'
    SQLALCHEMY_TRACK_MODIFICATION = False
