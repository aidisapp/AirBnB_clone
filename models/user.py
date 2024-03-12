#!/usr/bin/python3
# Authors: Idongesit Ekanem

"""
    This module defines a User Class
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    This represents a class for managing
    user objects
    """

    first_name = ""
    last_name = ""
    email = ""
    password = ""
