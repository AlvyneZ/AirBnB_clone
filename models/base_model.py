#!/usr/bin/python3
"""
This "base_model.py" module defines one class:
    BaseModel - defines all common attributes/methods for other classes
"""
import uuid
from datetime import datetime
from . import storage


class BaseModel:
    """
    Class that defines a base class to defines all common
     attributes/methods for other classes

    Attrs:
        self.id (string): UUID identifier of a base instance
        self.created_at (datetime): assigned the current datetime when an
         instance is created
        self.updated_at (datetime): assigned the created_at time at creation
         and is updated when the instance is changed

    Methods:
        save: updates the public instance attribute updated_at
        to_dict: Coverts an instance of BaseModel to a dictionary
    """

    def __init__(self, *args, **kwargs):
        """
        Initializer for setting BaseModel identifier & timestamps

        Args:
            args (tuple): positional arguments (not used)
            kwargs (dict): keyword arguments
        """
        if kwargs is not None and len(kwargs) != 0:
            DATETIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, DATETIME_FORMAT)
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        Returns a string representation of the current BaseModel instance
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            str(self.__dict__)
        )

    def save(self):
        """
        Updates the public instance attribute updated_at
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Coverts an instance of BaseModel to a dictionary

        Returns:
            dictionary representation of BaseModel instance
        """
        dict_rep = self.__dict__.copy()
        dict_rep["__class__"] = self.__class__.__name__
        DATETIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"
        dict_rep["created_at"] = datetime.strftime(
            self.created_at, DATETIME_FORMAT)
        dict_rep["updated_at"] = datetime.strftime(
            self.updated_at, DATETIME_FORMAT)
        return dict_rep
