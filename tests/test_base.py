#!/usr/bin/python3
"""
This "test_base.py" module defines one class:
    TestBase: for testing the functionality of the Base class

Run from project directory using:
$   python3 -m unittest ./tests/test_base.py
"""
import os

import unittest

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """
    Class for testing the functionality of the Base class

    Methods:
        tearDown: resets parameters at the end of tests
        test_init: tests identifier incrementing and setting
        test_to_json_string: tests to_json_string method
        test_from_json_string: tests from_json_string method
        test_create: tests the create method
        test_save_to_file: tests the save_to_file method of Base class
        test_load_from_file: tests the load_from_file method of Base class
    """

    def tearDown(self):
        """
        Runs at the end of each test to reset Base identifier count
        """
        Base._Base__nb_objects = 0
        return super().tearDown()

    def test_init(self):
        """
        Test for checking the setting of instance id and incrementing
         of __nb_objects
        """
        b1 = Base()
        b2 = Base()
        b3 = Base(None)
        b4 = Base(12)
        b5 = Base("str")
        b6 = Base()
        b7 = Base([1, 2, 3])

        self.assertEqual(
            b1.id, 1,
            "initializer should set id of first object to 1")
        self.assertEqual(
            b2.id, 2,
            "initializer should increment id for subsequent objects")
        self.assertEqual(
            b3.id, 3,
            "initializer should increment id for subsequent objects")
        self.assertEqual(
            b4.id, 12,
            "initializer should set id with the provided value")
        self.assertEqual(
            b5.id, "str",
            "initializer should set id with the provided value")
        self.assertEqual(
            b6.id, 4,
            "initializer should increment id for subsequent objects")
        self.assertEqual(
            b7.id, [1, 2, 3],
            "initializer should set id with the provided value")
        self.assertEqual(
            Base._Base__nb_objects, 4,
            "Recorded number of objects should equal objects "
            "initialized with id not set")

    def test_to_json_string(self):
        """
        Test for to_json_string method of Base class
        """
        self.assertEqual(
            Base.to_json_string(None),
            "[]",
            "converter should return a JSON of an empty list for None arg"
        )
        self.assertEqual(
            Base.to_json_string([]),
            "[]",
            "converter should return a JSON of an empty list for [] arg"
        )
        self.assertEqual(
            Base.to_json_string([{"a": 1, "b": 2}]),
            """[{"a": 1, "b": 2}]"""
        )
        self.assertEqual(
            Base.to_json_string([{"a": 1, "b": 2}, {"c": 3}]),
            """[{"a": 1, "b": 2}, {"c": 3}]"""
        )

    def test_from_json_string(self):
        """
        Test for from_json_string method of Base class
        """
        self.assertListEqual(
            Base.from_json_string(None),
            [],
            "converter should return an empty list for None arg"
        )
        self.assertListEqual(
            Base.from_json_string("[]"),
            [],
            "converter should return an empty list for [] arg"
        )
        self.assertListEqual(
            Base.from_json_string("""[{"a": 1, "b": 2}]"""),
            [{"a": 1, "b": 2}]
        )
        self.assertListEqual(
            Base.from_json_string("""[{"a": 1, "b": 2}, {"c": 3}]"""),
            [{"a": 1, "b": 2}, {"c": 3}]
        )

    def test_create(self):
        """
        Test for create method of Base class
        """
        r1 = Rectangle(1, 2, 3, 4)
        dr1 = r1.to_dictionary()
        r2 = Rectangle.create(**dr1)
        self.assertEqual(r1.__str__(), r2.__str__())
        self.assertEqual(r1 == r2, False)
        self.assertEqual(r1 is r2, False)

        s1 = Square(1, 2, 3)
        ds1 = s1.to_dictionary()
        s2 = Square.create(**ds1)
        self.assertEqual(s1.__str__(), s2.__str__())
        self.assertEqual(s1 == s2, False)
        self.assertEqual(s1 is s2, False)

    def __backup_og_files(self):
        """
        For backing up original files
        """
        sq_file_existed = False
        rct_file_existed = False
        if os.path.exists("Square.json"):
            os.rename("Square.json", "Square.json_bkp_test")
            sq_file_existed = True
        if os.path.exists("Rectangle.json"):
            os.rename("Rectangle.json", "Rectangle.json_bkp_test")
            rct_file_existed = True
        return (sq_file_existed, rct_file_existed)

    def __restore_og_files(self, sq_file_existed, rct_file_existed):
        """
        For restoring original files
        """
        if sq_file_existed:
            os.rename("Square.json_bkp_test", "Square.json")
        if rct_file_existed:
            os.rename("Rectangle.json_bkp_test", "Rectangle.json")

    def __save_file(self):
        """
        For saving objects to a file for testing save and load
        """
        r1 = Rectangle(2, 3, 4, 5, 1)
        r2 = Rectangle(7, 8, 9, 0, 6)
        lr = [r1, r2]
        Rectangle.save_to_file(lr)
        s1 = Square(3, 4, 5, 2)
        s2 = Square(8, 9, 0, 7)
        ls = [s1, s2]
        Square.save_to_file(ls)
        return (lr, ls)

    def __delete_file(self):
        """
        For deleting files used for testing
        """
        if os.path.exists("Square.json"):
            os.remove("Square.json")
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

    def test_save_to_file(self):
        """
        Test for save_to_file method of Base class
        """
        files_existed = self.__backup_og_files()
        try:
            Rectangle.save_to_file(None)
            with open("Rectangle.json", "r", encoding="utf-8") as file:
                self.assertEqual("[]", file.read())
            self.__delete_file()

            Rectangle.save_to_file([])
            with open("Rectangle.json", "r", encoding="utf-8") as file:
                self.assertEqual("[]", file.read())
            self.__delete_file()

            Rectangle.save_to_file([Rectangle(5, 4, 3, 2, 1)])
            with open("Rectangle.json", "r", encoding="utf-8") as file:
                self.assertEqual(
                    """[{"id": 1, "width": 5, "height": 4, "x": 3, "y": 2}]""",
                    file.read()
                )

            self.__save_file()
            with open("Rectangle.json", "r", encoding="utf-8") as file:
                self.assertEqual(
                    """[{"id": 1, "width": 2, "height": 3, "x": 4, "y": 5},"""
                    """ {"id": 6, "width": 7, "height": 8, "x": 9, "y": 0}]""",
                    file.read()
                )
            with open("Square.json", "r", encoding="utf-8") as file:
                self.assertEqual(
                    """[{"id": 2, "size": 3, "x": 4, "y": 5},"""
                    """ {"id": 7, "size": 8, "x": 9, "y": 0}]""",
                    file.read()
                )
        finally:
            self.__delete_file()
            self.__restore_og_files(*files_existed)

    def test_load_from_file(self):
        """
        Test for load_from_file method of Base class
        """
        files_existed = self.__backup_og_files()
        try:
            self.assertListEqual(
                Rectangle.load_from_file(),
                []
            )

            lr_og, ls_og = self.__save_file()
            lr = Rectangle.load_from_file()
            ls = Square.load_from_file()
            for i in range(len(lr_og)):
                self.assertEqual(lr[i].__str__(), lr_og[i].__str__())
            for i in range(len(ls_og)):
                self.assertEqual(ls[i].__str__(), ls_og[i].__str__())
        finally:
            self.__delete_file()
            self.__restore_og_files(*files_existed)
