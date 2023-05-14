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
        all: returns the dictionary __objects
        new: sets in __objects the obj with key <obj class name>.id
        save: serializes __objects to the JSON file (path: __file_path)
        reload: deserializes the JSON file to __objects
        __objects_to_json: Coverts __objects to a json string
        __objects_from_json: Coverts a json string to instances in __objects
        __objects_populate: Converts a dictionary to instances in __objects
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        Adds a new object to the dictionary __objects
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def __objects_to_json(self):
        """
        Coverts __objects (dictionary of BaseModel instances) to
         a dictionary of instance dictionaries and to a JSON string

        Returns:
            json string representation of __objects
        """
        dict_objs = {}
        if len(self.__objects) > 0:
            for key, val in self.__objects.items():
                dict_objs[key] = val.to_dict()
        return json.dumps(dict_objs)

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        with open(self.__file_path, "w", encoding="utf-8") as file:
            file.write(self.__objects_to_json())

    def __objects_from_json(self, json_string):
        """
        Deserializes a JSON string into the __objects attribute

        Args:
            json_string: json string to be converted
        """
        self.__objects = {}
        if json_string is not None:
            dict_objs = {}
            dict_objs = json.loads(json_string)
            if len(dict_objs) > 0:
                self.__objects_populate(dict_objs)

    def __objects_populate(self, dict_objs):
        """
        Converts a dictionary entry to the corresponding class instance
        """
        from models.base_model import BaseModel

        for key, val in dict_objs.items():
            class_name, id = key.split(".")
            if class_name == "BaseModel":
                self.__objects[key] = BaseModel(**val)

    def reload(self):
        """
        Loads JSON representation of class instances from file and creates
         the list of objects

        Returns:
            List of loaded objects inheriting from BaseModel
        """
        try:
            with open(self.__file_path, "r", encoding="utf-8") as file:
                content = file.read()
                self.__objects_from_json(content)
        except FileNotFoundError:
            pass
