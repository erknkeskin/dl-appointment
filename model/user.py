from app import db


class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_fullname = db.Column(db.String, nullable=False)
    user_email = db.Column(db.String, nullable=False)
    user_password = db.Column(db.String, nullable=False)
    user_created = db.Column(db.DateTime, nullable=False)
    user_modified = db.Column(db.DateTime, nullable=False)
    user_status = db.Column(db.Integer, nullable=False, default=1)