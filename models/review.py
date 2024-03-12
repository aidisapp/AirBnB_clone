#!/usr/bin/python3
# Authors: Idongesit Ekanem

"""
    This module defines a Review Class
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    This represents a class for managing
    Review objects
    """

    user_id = ""
    place_id = ""
    text = ""
