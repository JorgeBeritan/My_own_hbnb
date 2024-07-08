import sys
sys.path.insert(0, "/home/kbit/Desktop/My_own_hbnb/hbnb")
import uuid
from config import db

class Amenity(db.Model):
    __tablename__ = "Amenities"

    id = db.Column(db.String(36), primary_key=True, nullable=False)
    name = db.Column(db.String(70), nullable=False)

    def __init__(
        self,
        name
        ):
        self.id = str(uuid.uuid4())
        self.name = name

    def __repr__(self):
        return f"<Amenity[{self.id}: {self.name}]>"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
            }
        
class PlaceAmenites(db.Model):

    __tablename__ = 'place amenities'

    id = db.Column(db.String(36) primary_key=True, nullable= False)
    place_id = db.Column(db.String(36) nullable=False)
    amenity_id = db.Column(db.String(36) nullable=False)

    def __init__(
        self.id = id
        self.place_id = place_id
        self.amenity_id = amenity_id
    ):
        self.id = str(uuid.uuid4())
        self.place_id = str(uuid.uuid4())
        self.amenity_id = str(uuid.uuid4())
    
    def __repr__(self):
        return f"<PlaceAmenity ({self.place_id} - {self.amenity_id})>"

    def to_dict(self):
        return {
            "id": self.id,
            "place_id" self.place_id,
            "amenity_id" self.amenity_id
        }
    