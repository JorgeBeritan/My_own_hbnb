import sys
sys.path.insert(0, "/home/kbit/Desktop/My_own_hbnb/hbnb")
from config import db
import uuid

class Place(db.Model):
    __tablename__ = "Places"

    id = db.Column(db.String(36), primary_key=True, nullable=False)
    name = db.Column(db.String(70), nullable=False)
    description = db.Column(db.Text, nullable=False)
    number_of_rooms = db.Column(db.Integer, nullable=False)
    number_of_bathrooms = db.Column(db.Integer, nullable=False)
    max_guest = db.Column(db.Integer, nullable=False)
    price_per_night = db.Column(db.Float, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    host_id = db.Column(db.String(36), db.ForeignKey('users.id'))
    city_id = db.Column(db.String(36), db.ForeignKey('Cities.id'))


    def __init__(
        self,
        name,
        description,
        number_of_rooms,
        number_of_bathrooms,
        max_guest,
        price_per_night,
        latitude,
        longitude,
        host_id,
        city_id
        ):
        self.id = str(uuid.uuid4())
        self.name = name
        self.description = description
        self.number_of_rooms = number_of_rooms
        self.number_of_bathrooms = number_of_bathrooms
        self.max_guest = max_guest
        self.price_per_night = price_per_night
        self.latitude = latitude
        self.longitude = longitude
        self.host_id = host_id
        self.city_id = city_id

    def __repr__(self):
        return f"<City[{self.id}: {self.name}]>"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "number_of_rooms": self.number_of_rooms,
            "number_of_bathrooms": self.number_of_bathrooms,
            "max_guest": self.max_guest,
            "price_per_night": self.price_per_night,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "host_id": self.host_id,
            "city_id": self.city_id
            }
