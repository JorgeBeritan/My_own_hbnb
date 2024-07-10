import sys
sys.path.insert(0, "/home/kbit/Desktop/My_own_hbnb/hbnb/persistence")
sys.path.insert(1, "/home/kbit/Desktop/My_own_hbnb/hbnb/models")
from user import User
from user_persistence import UserPersistence

class UserService:

    @staticmethod
    def create_user(email, first_name, last_name, password, is_admin=False):
        new_user = User(email, first_name, last_name, password, is_admin)
        UserPersistence.add_user(new_user)
        return new_user

    @staticmethod
    def get_all_user():
        return UserPersistence.get_users()

    @staticmethod
    def get_user_by_id(user_id):
        user = UserPersistence.get_user_by_id(user_id)
        return user

    @staticmethod
    def update_user(user_id, email, first_name, last_name):
        user = UserPersistence.get_user_by_id(user_id)
        if user:
            if email:
                user.email = email
            if first_name:
                user.first_name = first_name
            if last_name:
                user.last_name = last_name
            UserPersistence.update_user(user)
            return user
        return None

    @staticmethod
    def delete_user(user_id):
        user = UserPersistence.get_user_by_id(user_id)
        if user:
            UserPersistence.delete_user(user)
            return True
        return False

    @staticmethod
    def filter_user_by_email(user_email):
        user = UserPersistence.filter_user_by_email(user_email)
        return user

