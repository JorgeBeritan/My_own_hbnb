import sys
sys.path.insert(0, "/home/kbit/Desktop/My_own_hbnb/hbnb")
sys.path.insert(1, "/home/kbit/Desktop/My_own_hbnb/hbnb/models")
from amenity import Amenity
from config import db

class AmenityPersistence:

    @staticmethod
    def add_amenity(amenity):
        db.session.add(amenity)
        db.session.commit()

    @staticmethod
    def get_amenities():
        return Amenity.query.all()

    @staticmethod
    def get_amenity_by_id(amenity_id):
        amenity = Amenity.query.get(amenity_id)
        return amenity

    @staticmethod
    def update_amenity(amenity):
        db.session.commit()

    @staticmethod
    def delete_amenity(amenity):
        if amenity:
            db.session.delete(amenity)
            db.session.commit()
