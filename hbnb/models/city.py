import sys
sys.path.insert(0, "/home/kbit/Desktop/My_own_hbnb/hbnb")
sys.path.insert(1, "/home/kbit/Desktop/My_own_hbnb/hbnb/models")
import uuid
from config import db
from country import Country

class City(db.Model):
    __tablename__ = "Cities"
    id = db.Column(db.String(36), primary_key=True, nullable=False)
    name = db.Column(db.String(70), nullable=False)
    country_code = db.Column(db.String(2), db.ForeignKey('Countries.code'),
                             nullable=False)

    def __init__(
        self,
        name,
        country_code
        ):
        self.id = str(uuid.uuid4())
        self.name = name
        self.country_code = country_code

    def __repr__(self):
        return f'<City[{self.id}: {self.name}]>'

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "country_code": self.country_code
            }
