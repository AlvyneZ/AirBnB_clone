#!/usr/bin/python3
"""
This "state.py" module defines one class:
    State(BaseModel) - defines attributes of a state
"""
from .base_model import BaseModel


class State(BaseModel):
    """
    Class that defines a State class to manage state details

    Attrs:
        name (string): Name of the State
    """
    name = ""
