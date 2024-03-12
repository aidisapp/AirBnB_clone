#!/usr/bin/python3
# Authors: Idongesit Ekanem

"""
    This module defines an User Class
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    This represents a class for managing
    City objects
    """

    state_id = ""
    name = ""
