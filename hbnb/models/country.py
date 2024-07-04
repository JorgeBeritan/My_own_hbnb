import sys
sys.path.insert(0, "/home/kbit/Desktop/My_own_hbnb/hbnb")
from config import db

class Country(db.Model):
    __tablename__ = "Countries"
    name = db.Column(db.String(70), nullable=False)
    code = db.Column(db.String(2), nullable=False, primary_key=True)

    def __init__(
            self,
            name,
            code
            ):
        self.name = name
        self.code = code

    def __repr__(self):
        return f"<Country[{self.code}: {self.name}]>"

    def to_dict(self):
        return {
            "name": self.name,
            "code": self.code 
                }
