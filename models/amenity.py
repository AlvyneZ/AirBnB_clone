#!/usr/bin/python3
"""
This "amenity.py" module defines one class:
    Amenity(BaseModel) - defines attributes of a amenity
"""
from .base_model import BaseModel


class Amenity(BaseModel):
    """
    Class that defines a Amenity class to manage amenity details

    Attrs:
        name (str): The name of the amenity.
    """

    name = ""
