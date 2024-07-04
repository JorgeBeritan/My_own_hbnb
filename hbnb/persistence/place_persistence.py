import sys
sys.path.insert(0, "/home/kbit/Desktop/My_own_hbnb/hbnb")
sys.path.insert(1, "/home/kbit/Desktop/My_own_hbnb/hbnb/models")
from config import db
from place import Place

class PlacePersistence:

    @staticmethod
    def add_place(place):
        db.session.add(place)
        db.session.commit()

    @staticmethod
    def get_places():
        return Place.query.all()

    @staticmethod
    def get_place_by_id(place_id):
        place = Place.query.get(place_id)
        return place

    @staticmethod
    def update_place(place):
        db.session.commit()

    @staticmethod
    def delete_place(place):
        if place:
            db.session.delete(place)
            db.session.commit()

