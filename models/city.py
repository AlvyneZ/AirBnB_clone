#!/usr/bin/python3
"""
This "city.py" module defines one class:
    City(BaseModel) - defines attributes of a city
"""
from .base_model import BaseModel


class City(BaseModel):
    """
    Class that defines a City class to manage city details

    Attrs:
        state_id (str): The state id.
        name (str): The name of the city.
    """

    state_id = ""
    name = ""
