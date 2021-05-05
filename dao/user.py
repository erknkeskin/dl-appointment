from model.user import User

class UserDao:

    @staticmethod
    def login(email, password):
        return User.query.filter(User.user_email==email, User.user_password==password, User.user_status == 1).first()


user_dao = UserDao()
