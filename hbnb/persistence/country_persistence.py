import sys
sys.path.insert(0, "/home/kbit/Desktop/My_own_hbnb/hbnb")
sys.path.insert(1, "/home/kbit/Desktop/My_own_hbnb/hbnb/models")
from config import db
from country import Country

class CountryPersistence:

    @staticmethod
    def add_country(country):
        db.session.add(country)
        db.session.commit()

    @staticmethod
    def get_countries():
        return Country.query.all()

    @staticmethod
    def get_country_by_code(code):
        country = Country.query.get(code)
        return country

    @staticmethod
    def update_country(country):
        db.session.commit()

    @staticmethod
    def delete_country(country):
        if country:
            db.session.delete(country)
            db.session.commit()
