#!/usr/bin/python3

import uuid

class Place:

    def __init__(self, name, description, number_of_rooms, number_of_bathrooms, max_guest, price_per_night, latitude, longitude, host_id, city_id):
        self.__id = str(uuid.uuid4())
        self.name = name
        self.description = description
        self.number_of_rooms = number_of_rooms
        self.number_of_bathrooms = number_of_bathrooms
        self.max_guest = max_guest
        self.price_per_night = price_per_night
        self.latitude = latitude
        self.longitude = longitude
        self.host_id = host_id
        self.city_id = city_id


    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, id):
        if type(id) is not str:
            raise ValueError("The id must be a string")
        
        self.__id = id

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        if type(name) is not str:  
            raise TypeError("The name must be a string")
        if name == "":
            raise ValueError("The name is required")
        self.__name = name

    @property
    def description(self):
        return self.__description
    
    @description.setter
    def description(self, value):
        if type(value) is not str:
            raise TypeError("The description must be a string")
        if value == "":
            raise ValueError("The description must be required")
        self.__description = value

    @property
    def number_of_rooms(self):
        return self.__number_of_rooms
    
    @number_of_rooms.setter
    def number_of_rooms(self, value):
        if type(value) is not int:
            raise TypeError("The number of rooms must be an integer")
        if value < 0:
            raise ValueError("The number of rooms must be a positive number")
        self.__number_of_rooms = value

    @property
    def number_of_bathrooms(self):
        return self.__number_of_bathrooms
    
    @number_of_bathrooms.setter
    def number_of_bathrooms(self, value):
        if type(value) is not int:
            raise TypeError("The number of bathrooms must be an integer")
        if value < 0:
            raise ValueError("The number of bathrooms must be a integer")
        
        self.__number_of_bathrooms = value

    @property
    def max_guest(self):
        return self.__max_guest
    
    @max_guest.setter
    def max_guest(self, value):
        if type(value) is not int:
            raise TypeError("The max guest must be a integer")
        if value < 0:
            raise ValueError("The max guest must be a positive number")
        self.__max_guest = value

    @property
    def price_per_night(self):
        return self.__price_per_night
    
    @price_per_night.setter
    def price_per_night(self, value):
        if type(value) is not float:
            raise TypeError("Price per night must be a float")
        if value < 0:
            raise ValueError("Price per night must be a positive number")
        self.__price_per_night = value

    @property
    def latitude(self):
        return self.__latitude 
    
    @latitude.setter
    def latitude(self, value):
        if type(value) is not float:
            raise TypeError("The latitude must be a float")
        self.__latitude = value

    @property
    def longitude(self):
        return self.__longitude

    @longitude.setter
    def longitude(self, value):
        if type(value) is not float:
            raise TypeError("Longitude must be a float")
        
        self.__longitude = value 