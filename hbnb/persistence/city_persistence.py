import sys
sys.path.insert(0, "/home/kbit/Desktop/My_own_hbnb/hbnb")
sys.path.insert(1, "/home/kbit/Desktop/My_own_hbnb/hbnb/models")
from config import db
from city import City

class CityPersistence:

    @staticmethod
    def add_city(city):
        db.session.add(city)
        db.session.commit()

    @staticmethod
    def get_cities():
        return City.query.all()

    @staticmethod
    def get_city_by_id(city_id):
        city = City.query.get(city_id)
        return city

    @staticmethod
    def update_city(city):
        db.session.commit()

    @staticmethod
    def delete_city(city):
        if city:
            db.session.delete(city)
            db.session.commit()
