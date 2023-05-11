#!/usr/bin/python3
"""
This "file_storage.py" module defines one class:
    FileStorage -  serializes instances to a JSON file and deserializes
     JSON file to instances
"""
import json


class FileStorage:
    """
    Class that serializes instances to a JSON file and deserializes
     JSON file to instances

    Attrs:
        __file_path (string): path to the JSON file
        __objects (dictionary): stores all objects by <class name>.id

    Methods:
        to_json_string: Coverts a list of dictionaries to a json string
        from_json_string: Coverts a json string to a list of dictionaries
        create: Converts a dictionary to the corresponding class instance
        save_to_file: Writes a JSON string of list of objects to a file
        load_from_file: Loads and creates class instances from JSON file
    """


    def __init__(self, *args, **kwargs):
        """
        Initializer for setting base identifier

        Args:
            id (integer): identifier of a base instance
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Coverts a list of dictionaries to a json string

        Args:
            list_dictionaries: object to be converted

        Returns:
            json string representation of list of dicttionaries
        """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
        Coverts a json string to a list of dictionaries

        Args:
            json_string: json string to be converted

        Returns:
            The original jsonified list of dictionaries
        """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Converts a dictionary to the corresponding class instance
        """
        from .rectangle import Rectangle
        from .square import Square

        if cls.__name__ == "Rectangle":
            obj = Rectangle(1, 1, id=100)
        elif cls.__name__ == "Square":
            obj = Square(1, id=100)
        else:
            obj = Base(id=100)
        obj.update(**dictionary)
        return obj

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes a JSON string representation of list of objects to a file

        Args:
            list_objs: List of objects inheriting from Base
        """
        file_name = "{}.json".format(cls.__name__)
        if list_objs is None:
            list_dicts = []
        else:
            list_dicts = [obj.to_dictionary() for obj in list_objs]
        json_str = cls.to_json_string(list_dicts)
        with open(file_name, "w", encoding="utf-8") as file:
            file.write(json_str)

    @classmethod
    def load_from_file(cls):
        """
        Loads JSON representation of class instances from file and creates
         a list of objects

        Returns:
            List of loaded objects inheriting from Base
        """
        file_name = "{}.json".format(cls.__name__)

        try:
            with open(file_name, "r", encoding="utf-8") as file:
                content = file.read()
                list_dicts = cls.from_json_string(content)
        except FileNotFoundError:
            return []

        return [cls.create(**obj_dict) for obj_dict in list_dicts]
