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

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        with open(self.__file_path, "w", encoding="utf-8") as file:
            # Converting __objects to dict of dictionaries
            dict_objs = {}
            if len(self.__objects) > 0:
                for key, val in self.__objects.items():
                    dict_objs[key] = val.to_dict()
            file.write(json.dumps(dict_objs))

    def reload(self):
        """
        Loads JSON representation of class instances from file and creates
         the list of objects

        Returns:
            List of loaded objects inheriting from BaseModel
        """
        from models.base_model import BaseModel
        from models.user import User

        try:
            with open(self.__file_path, "r", encoding="utf-8") as file:
                json_string = file.read()
                # Converting read string to dictionary of dicts
                self.__objects = {}
                if json_string is not None:
                    dict_objs = {}
                    dict_objs = json.loads(json_string)
                    if len(dict_objs) > 0:
                        # Converts dict entries to the class instances
                        for key, val in dict_objs.items():
                            class_name = val["__class__"]
                            del(val["__class__"])
                            self.__objects[key] = eval(class_name)(**val)
        except FileNotFoundError:
            pass
