#!/usr/bin/python3
"""
This "user.py" module defines one class:
    User(BaseModel) - defines attributes of a user
"""
from .base_model import BaseModel


class User(BaseModel):
    """
    Class that defines a User class to manage user details

    Attrs:
        email (string): User email account
        password (string): User's password for account
        first_name (string): First name of the User
        last_name (string): Last nmae of the User
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
