import sys
sys.path.insert(0, "/home/kbit/Desktop/My_own_hbnb/hbnb/models")
sys.path.insert(1, "/home/kbit/Desktop/My_own_hbnb/hbnb/persistence")
from place import Place
from place_persistence import PlacePersistence

class PlaceService:

    @staticmethod
    def create_place(
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
        new_place = Place(
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
            )
        PlacePersistence.add_place(new_place)
        return new_place

    @staticmethod
    def get_all_place():
        return PlacePersistence.get_places()

    @staticmethod
    def get_place_by_id(place_id):
        place = PlacePersistence.get_place_by_id(place_id)
        return place

    @staticmethod
    def update_place(
        place_id,
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
        place = PlacePersistence.get_place_by_id(place_id)
        if place:
            if name:
                place.name = name
            if description:
                place.description = description
            if number_of_rooms:
                place.number_of_rooms = number_of_rooms
            if number_of_bathrooms:
                place.number_of_bathrooms = number_of_bathrooms
            if max_guest:
                place.max_guest = max_guest
            if price_per_night:
                place.price_per_night = price_per_night
            if latitude:
                place.latitude = latitude
            if longitude:
                place.longitude = longitude
            if host_id:
                place.host_id = host_id
            if city_id:
                place.city_id = city_id
            PlacePersistence.update_place(place)
            return place
        return None

    @staticmethod
    def delete_place(place_id):
        place = PlacePersistence.get_place_by_id(place_id)
        if place:
            PlacePersistence.delete_place(place)
            return True
        return False
