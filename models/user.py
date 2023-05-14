#!/usr/bin/python3
"""
This "user.py" module defines one class:
    User(BaseModel) - defines all common attributes/methods for other classes
"""
from .base_model import BaseModel


class User(BaseModel):
    """
    Class that defines a User class to manage user details

    Attrs:
        self.email (string): User email account
        self.password (string): User's password for account
        self.first_name (string): First name of the User
        self.last_name (string): Last nmae of the User
    """

    def __init__(self, *args, **kwargs):
        """
        Initializer for setting BaseModel identifier & timestamps

        Args:
            args (tuple): positional arguments (not used)
            kwargs (dict): keyword arguments
        """
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
        super().__init__(*args, **kwargs)
