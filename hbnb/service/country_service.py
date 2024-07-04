import sys
sys.path.insert(0, "/home/kbit/Desktop/My_own_hbnb/hbnb/persistence")
sys.path.insert(1, "/home/kbit/Desktop/My_own_hbnb/hbnb/models")
from country import Country
from country_persistence import CountryPersistence

class CountryService:

    @staticmethod
    def create_country(name, code):
        new_country = Country(name, code)
        CountryPersistence.add_country(new_country)
        return new_country

    @staticmethod
    def get_all_countries():
        return CountryPersistence.get_countries()

    @staticmethod
    def get_country_by_code(code):
        country = CountryPersistence.get_country_by_code(code)
        return country

    @staticmethod
    def update_country(code, name):
        country = CountryPersistence.get_country_by_code(code)
        if country:
            if code:
                country.code = code
            if name:
                country.name = name
            CountryPersistence.update_country(country)
            return country
        return None

    @staticmethod
    def delete_country(code):
        country = CountryPersistence.get_country_by_code(code)
        if country:
            CountryPersistence.delete_country(country)
            return True
        return False

