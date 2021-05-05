import os
import socket

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    if socket.gethostname() == 'erkankeskin-pc':
        SQLALCHEMY_DATABASE_URI = 'postgresql://erkan:123@localhost/appointmentdb1'
    else:
        SQLALCHEMY_DATABASE_URI = 'postgresql://admin_appousr:1lq3PZlnmR@localhost/admin_appointmentdb1'

    SQLALCHEMY_TRACK_MODIFICATION = False
