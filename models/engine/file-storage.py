#!/usr/bin/python3
"""
Module for FileStorage class
This module contains the FileStorage class responsible for
serializing instances to a JSON file and deserializing JSON files to instances.
"""

import json


class FileStorage:
    """
    File storage class
    """
    
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

    def reload(self):
        """
        Deserialize the JSON file (__file_path) to __objects
        if the file exists.
        """
        try:
            with open(self.__file_path, 'r') as f:
                self.__objects = json.load(f)
        except FileNotFoundError:
            pass
