import sys
sys.path.insert(0, "/home/kbit/Desktop/My_own_hbnb/hbnb")
sys.path.insert(1, "/home/kbit/Desktop/My_own_hbnb/hbnb/models")
from config import db
from user import User

class UserPersistence:

    @staticmethod
    def add_user(user):
        db.session.add(user)
        db.session.commit()

    @staticmethod
    def get_users():
        return User.query.all()

    @staticmethod
    def get_user_by_id(user_id):
        user = User.query.get(user_id)
        return user

    @staticmethod
    def update_user(user):
        db.session.commit()

    @staticmethod
    def delete_user(user):
        if user:
            db.session.delete(user)
            db.session.commit()

