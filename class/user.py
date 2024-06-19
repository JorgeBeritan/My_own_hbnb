#!/usr/bin/python3

import uuid
from datetime import datetime
from validator import email_validator

class User:

    __emails = set()

    def __init__(self, email, first_name, last_name):
        self.__id = str(uuid.uuid4())
        self.email = email
        self.first_name = first_name
        self.last_name = last_name

    @property
    def id (self):
        return self.__id
    
    @id.setter
    def id(self, id):
        if type(id) is not str:
            raise TypeError("The id must be a string")
        if id == "":
            raise ValueError("Something wrong here")
        self.__id = id

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        if type(email) is not str:
            raise TypeError("The email must be a string")
        if not email_validator(email):
            raise ValueError("The email is not valid")
        if email == "":
            raise ValueError("Something wrong here")
        
        self.__email = email

    @property
    def first_name(self):
        return self.__first_name
    
    @first_name.setter
    def first_name(self, value):
        if type(value) is not str:
            raise TypeError("The first name must be a string")
        if value == "":
            raise ValueError("The name is required")
        
        self.__first_name = value

    @property
    def last_name(self):
        return self.__last_name
    
    @last_name.setter
    def last_name(self, value):
        if type(value) is not str:
            raise TypeError("The last name must be string")
        if value == "":
            raise ValueError("The last name is required")
        
        self.__last_name = value
