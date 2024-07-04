import sys
sys.path.insert(0, "/home/kbit/Desktop/My_own_hbnb/hbnb/persistence")
sys.path.insert(1, "/home/kbit/Desktop/My_own_hbnb/hbnb/models")
from city import City
from city_persistence import CityPersistence

class CityService:

    @staticmethod
    def create_city(name, country_code):
        new_city = City(name, country_code)
        CityPersistence.add_city(new_city)
        return new_city

    @staticmethod
    def get_all_cities():
        return CityPersistence.get_cities()

    @staticmethod
    def get_city_by_id(city_id):
        city = CityPersistence.get_city_by_id(city_id)
        return city

    @staticmethod
    def update_city(city_id, name, country_code):
        city = CityPersistence.get_city_by_id(city_id)
        if city:
            if name:
                city.name = name
            if country_code:
                city.country_code = country_code
            CityPersistence.update_city(city)
            return city
        return None

    @staticmethod
    def delete_city(city_id):
        city = CityPersistence.get_city_by_id(city_id)
        if city:
            CityPersistence.delete_city(city)
            return True
        return False
