#!/usr/bin/python3
# Authors: Idongesit Ekanem

"""
    This module defines a Place Class
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """
    This represents a class for managing
    Place objects
    """

    name = ""
    city_id = ""
    user_id = ""
    description = ""
    latitude = 0.0
    longitude = 0.0
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    amenity_ids = []
