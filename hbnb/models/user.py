import uuid
from config import db
from config import bcrypt

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.String(36), primary_key=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    def __init__(
        self,
        email,
        first_name,
        last_name,
        password,
        is_admin
        ):
        self.id = str(uuid.uuid4())
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.is_admin = bool(is_admin)

    def __repr__(self):
        return f'<User[{self.id}: {self.email}]'

    def to_dict(self):
        return {
            "id": self.id,
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "is_admin": self.is_admin,
            }

    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)

