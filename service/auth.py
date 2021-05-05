from flask import session,request, jsonify
from validate_email import validate_email
from dao.user import user_dao

class AuthService:

    @staticmethod
    def logout():
        session.pop('logged')
        session.pop('user_fullname')
        session.pop('user_email')
        return True

    @staticmethod
    def is_logged():
        if 'logged' in session:
            return True
        else:
            return False

    @staticmethod
    def login():
        email = request.form.get('email')
        password = request.form.get('password')


        if not validate_email(email):
            return jsonify({'status': 'error', 'message': 'e-mail hatalıdır!'})

        if password == '':
            return jsonify({'status': 'error', 'message': 'şifre boş olamaz!'})

        user = user_dao.login(email, password)

        if user is None:
            return jsonify({'status': 'error', 'message': 'kullanıcı bulunamadı!'})
        else:
            session['logged'] = 'logged'
            session['user_fullname'] = user.user_fullname
            session['user_email'] = user.user_email

            return jsonify({'status': 'ok', 'message': 'giriş başarılı'})

auth_service =  AuthService()
            