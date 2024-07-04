import sys
sys.path.insert(0, "/home/kbit/Desktop/My_own_hbnb/hbnb/models")
sys.path.insert(1, "/home/kbit/Desktop/My_own_hbnb/hbnb/persistence")
from amenity import Amenity
from amenity_persistence import AmenityPersistence

class AmenityService:

    @staticmethod
    def create_amenity(name):
        new_amenity = Amenity(name)
        AmenityPersistence.add_amenity(new_amenity)
        return new_amenity

    @staticmethod
    def get_all_amenity():
        return AmenityPersistence.get_amenities()

    @staticmethod
    def get_amenity_by_id(amenity_id):
        amenity = AmenityPersistence.get_amenity_by_id(amenity_id)
        return amenity

    @staticmethod
    def update_amenity(amenity_id, name):
        amenity = AmenityPersistence.get_amenity_by_id(amenity_id)
        if amenity:
            if name:
                amenity.name = name
            AmenityPersistence.update_amenity(amenity)
            return amenity
        return None

    @staticmethod
    def delete_amenity(amenity_id):
        amenity = AmenityPersistence.get_amenity_by_id(amenity_id)
        if amenity:
            AmenityPersistence.delete_amenity(amenity)
            return True
        return False


