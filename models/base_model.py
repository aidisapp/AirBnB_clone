#!/usr/bin/python3
"""Module for BaseModel class
This module contains the BaseModel class representing the base model
for all other classes. It contains common attributes and methods."""

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """This class represents the base model of the object hierarchy."""

    def __init__(self, *args, **kwargs):
        """This method initializes a Base instance.

        Args:
            - *args: list of arguments
            - **kwargs: dict of key-value arguments
        """

        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """This method returns a human-readable
        string representation of an instance."""
        return "[{}] ({}) {}".format(type(
                    self).__name__, self.id, self.__dict__
                    )

    def save(self):
        """This method updates the updated_at attribute
        with the current datetime."""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """This method returns a dictionary representation of an instance."""
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
