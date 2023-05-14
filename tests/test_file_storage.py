#!/usr/bin/python3
"""
This "test_base_model.py" module defines one class:
    TestBaseModel: for testing the functionality of the BaseModel class

Run from project directory using:
$   python3 -m unittest ./tests/test_file_storage.py
"""
from base64 import b32decode
import os
import json

import unittest

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel, storage


class TestBaseModel(unittest.TestCase):
    """
    Class for testing the functionality of the BaseModel class

    Methods:
        tearDown: resets parameters at the end of tests
        test_save_to_file: tests the save method of BaseModel class
        test_load_from_file: tests the reload method of BaseModel class
    """

    def tearDown(self):
        """
        Runs at the end of each test to reset FileStorage objects
        """
        storage._FileStorage__objects = {}
        return super().tearDown()
        
    def __backup_og_files(self):
        """
        For backing up original JSON file
        """
        file_existed = False
        if os.path.exists("file.json"):
            os.rename("file.json", "file.json_bkp_test")
            file_existed = True
        return file_existed

    def __restore_og_files(self, file_existed):
        """
        For restoring original files
        """
        if file_existed:
            os.rename("file.json_bkp_test", "file.json")

    def __save_file(self):
        """
        For saving objects to a file for testing save and load
        """
        # The init will add the models to the storage.__objects
        b1 = BaseModel()
        b2 = BaseModel()
        # Saving to storage
        storage.save()
        return (b1, b2)

    def __delete_file(self):
        """
        For deleting files used for testing
        """
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_save(self):
        """
        Test for save method of BaseModel class
        """
        file_existed = self.__backup_og_files()
        try:
            storage._FileStorage__objects = {}
            self.assertDictEqual(
                storage.all(), {},
                "Unit test needs to empty __objects and all() should reflect"
            )

            b1, b2 = self.__save_file()
            objs = storage.all()
            self.assertEqual(
                b1.__str__(),
                objs["BaseModel.{}".format(b1.id)].__str__())
            self.assertEqual(
                b2.__str__(),
                objs["BaseModel.{}".format(b2.id)].__str__())
            with open("file.json", "r", encoding="utf-8") as file:
                self.assertEqual(
                    '{{"BaseModel.{}": {}, "BaseModel.{}": {}}}'.format(
                        b1.id,
                        json.dumps(b1.to_dict()),
                        b2.id,
                        json.dumps(b2.to_dict())
                        ),
                    file.read()
                )
        finally:
            self.__delete_file()
            self.__restore_og_files(file_existed)

    def test_reload(self):
        """
        Test for reload method of BaseModel class
        """
        file_existed = self.__backup_og_files()
        try:
            storage._FileStorage__objects = {}
            self.assertDictEqual(
                storage.all(), {},
                "Unit test needs to empty __objects and all() should reflect"
            )

            b1, b2 = self.__save_file()

            storage._FileStorage__objects = {}
            self.assertDictEqual(
                storage.all(), {},
                "Unit test needs to empty __objects and all() should reflect"
            )

            storage.reload()
            objs = storage.all()
            self.assertEqual(
                b1.__str__(),
                objs["BaseModel.{}".format(b1.id)].__str__())
            self.assertEqual(
                b2.__str__(),
                objs["BaseModel.{}".format(b2.id)].__str__())
        finally:
            self.__delete_file()
            self.__restore_og_files(file_existed)
