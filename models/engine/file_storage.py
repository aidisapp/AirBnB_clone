#!/usr/bin/python3

"""
Module for FileStorage class
This module contains the FileStorage class responsible for
serializing instances to a JSON file and deserializing JSON files to instances.
"""

import json
import os
import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    File storage class
    """
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """
        Initialize the FileStorage instance.
        """
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """
        Return the dictionary __objects.
        """
        return self.__objects

    def new(self, obj):
        """
        Set __objects with the object as the value
        and its class name + id as the key.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj.to_dict()

    def save(self):
        """
        Serialize __objects to the JSON file (__file_path).
        """
        with open(self.__file_path, 'w') as f:
            json.dump(self.__objects, f)

    def classes(self):
        """
        Returns a dictionary of valid classes and their references
        """
        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
        }
        return classes

    def reload(self):
        """
        Deserialize the JSON file to __objects
        """
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, 'r') as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    class_name = key.split('.')[0]
                    if class_name in self.classes():
                        self.__objects[key] = self.classes()[class_name](
                                        **value)
