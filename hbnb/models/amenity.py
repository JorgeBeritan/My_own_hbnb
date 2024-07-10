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
