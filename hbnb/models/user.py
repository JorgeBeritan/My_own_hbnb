import sys
sys.path.insert(0, "/home/kbit/Desktop/My_own_hbnb/hbnbAPI")
sys.path.insert(1, "/home/kbit/Desktop/My_own_hbnb/hbnb")
import uuid
from config import db


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.String(36), primary_key=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)


    def __init__(
        self,
        email,
        first_name,
        last_name,
        ):
        self.id = str(uuid.uuid4())
        self.email = email
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return f'<User[{self.id}: {self.email}]'

    def to_dict(self):
        return {
            "id": self.id,
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name
            }

