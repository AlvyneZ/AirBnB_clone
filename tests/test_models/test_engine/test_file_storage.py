#!/usr/bin/python3
"""
This "test_base_model.py" module defines one class:
    TestBaseModel: for testing the functionality of the BaseModel class

Run from project directory using:
$   python3 -m unittest ./tests/test_models/test_engine/test_file_storage.py
"""
import os
import json

import unittest

from models.base_model import BaseModel, storage


class TestBaseModel(unittest.TestCase):
    """
    Class for testing the functionality of the BaseModel class

    Methods:
        tearDown: resets parameters at the end of tests
        test_all: tests the all method of BaseModel class
        test_save: tests the save method of BaseModel class
        test_new: tests the new method of BaseModel class
        test_reload: tests the reload method of BaseModel class
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
        self.assertEqual(
            storage._FileStorage__file_path, "file.json",
            "The file storage path should be 'file.json'"
        )
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
        b2.name = "Test"
        b2.save()
        # Saving to storage
        storage.save()
        return (b1, b2)

    def __delete_file(self):
        """
        For deleting files used for testing
        """
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_all(self):
        """
        Test for all method of BaseModel class
        """
        file_existed = self.__backup_og_files()
        try:
            storage._FileStorage__objects = {}
            self.assertDictEqual(
                storage.all(), {},
                "Unit test needs to empty __objects"
            )

            b1, b2 = self.__save_file()
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

    def test_new(self):
        """
        Test for new method of BaseModel class
        """
        file_existed = self.__backup_og_files()
        try:
            storage._FileStorage__objects = {}
            self.assertDictEqual(
                storage._FileStorage__objects, {},
                "Unit test needs to empty __objects"
            )

            b1 = BaseModel(
                id='219c8141-85ca-4f00-923b-5a3b47fc2517',
                created_at='2023-05-11T21:53:37.103600',
                updated_at='2023-05-11T21:53:37.103650')
            self.assertDictEqual(
                storage._FileStorage__objects, {},
                "Only new instances should be added to __objects upon init"
            )
            storage.new(b1)

            objs = storage._FileStorage__objects
            self.assertEqual(
                b1.__str__(),
                objs["BaseModel.{}".format(b1.id)].__str__())
        finally:
            self.__delete_file()
            self.__restore_og_files(file_existed)

    def test_save(self):
        """
        Test for save method of BaseModel class
        """
        file_existed = self.__backup_og_files()
        try:
            storage._FileStorage__objects = {}
            self.assertDictEqual(
                storage._FileStorage__objects, {},
                "Unit test needs to empty __objects"
            )

            b1, b2 = self.__save_file()
            objs = storage._FileStorage__objects
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
                storage._FileStorage__objects, {},
                "Unit test needs to empty __objects"
            )

            b1, b2 = self.__save_file()

            storage._FileStorage__objects = {}
            self.assertDictEqual(
                storage._FileStorage__objects, {},
                "Unit test needs to empty __objects"
            )

            storage.reload()
            objs = storage._FileStorage__objects
            self.assertEqual(
                b1.__str__(),
                objs["BaseModel.{}".format(b1.id)].__str__())
            self.assertEqual(
                b2.__str__(),
                objs["BaseModel.{}".format(b2.id)].__str__())
        finally:
            self.__delete_file()
            self.__restore_og_files(file_existed)
