#!/usr/bin/python3

"""
Module for BaseModel class
This module contains the BaseModel class representing the base model
for all other classes. It contains common attributes and methods.
"""

import uuid
from datetime import datetime


class BaseModel:
    """
    BaseModel class
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the BaseModel instance.
        If it's a new instance (not from a dictionary representation),
        add a call to the method new(self) on storage.
        """
        if kwargs:
            from models import storage  # Import storage here
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        setattr(self, key, datetime.strptime(
                            value, '%Y-%m-%dT%H:%M:%S.%f'))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            from models import storage  # Import storage here
            storage.new(self)  # Now you can use storage here

    def save(self):
        """
        Update the 'updated_at' attribute with the current datetime.
        Call save(self) method of storage.
        """
        self.updated_at = datetime.now()
        from models import storage  # Import storage here
        storage.save()  # Now you can use storage here

    def to_dict(self):
        """
        Return a dictionary representation of the BaseModel instance.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

    def __str__(self):
        """
        Return a string representation of the BaseModel instance.
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

