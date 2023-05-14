#!/usr/bin/python3
"""
This "test_base_model.py" module defines one class:
    TestBaseModel: for testing the functionality of the BaseModel class

Run from project directory using:
$   python3 -m unittest ./tests/test_models/test_base_model.py
"""
from datetime import datetime, timedelta
from uuid import UUID

import unittest

from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Class for testing the functionality of the BaseModel class

    Methods:
        tearDown: resets parameters at the end of tests
        test_init: tests BaseModel creation
        test_str: tests __str__ method
        test_save: tests save method
        test_to_dict: tests to_dict method
    """

    def test_init(self):
        """
        Test for checking the creation of BaseModel
        """
        c1 = datetime.now()
        b1 = BaseModel()
        c2 = datetime.now()
        b2 = BaseModel(
            id='219c8141-85ca-4f00-923b-5a3b47fc2517',
            created_at='2023-05-11T21:53:37.103600',
            updated_at='2023-05-11T21:53:37.103650')
        tc = datetime.strptime(
            '2023-05-11T21:53:37.103600',
            '%Y-%m-%dT%H:%M:%S.%f')
        tu = datetime.strptime(
            '2023-05-11T21:53:37.103650',
            '%Y-%m-%dT%H:%M:%S.%f')

        try:
            UUID(b1.id, version=4)
        except ValueError:
            self.fail("initializer should set a valid version4 UUID to id")
        self.assertGreaterEqual(
            (b1.created_at - c1) / timedelta(milliseconds=1), 0,
            "initializer should set created_at appropriately")
        self.assertGreaterEqual(
            (c2 - b1.created_at) / timedelta(milliseconds=1), 0,
            "initializer should set created_at appropriately")
        self.assertGreater(
            (b1.updated_at - b1.created_at) / timedelta(milliseconds=1), 0,
            "initializer should set updated_at appropriately")
        self.assertGreaterEqual(
            (b1.updated_at - c1) / timedelta(milliseconds=1), 0,
            "initializer should set updated_at appropriately")
        self.assertGreaterEqual(
            (c2 - b1.updated_at) / timedelta(milliseconds=1), 0,
            "initializer should set updated_at appropriately")
        self.assertEqual(
            b2.id, '219c8141-85ca-4f00-923b-5a3b47fc2517',
            "initializer should set the passed id value")
        self.assertEqual(
            (tc - b2.created_at) / timedelta(milliseconds=1), 0,
            "initializer should set the passed created_at value")
        self.assertEqual(
            (tu - b2.updated_at) / timedelta(milliseconds=1), 0,
            "initializer should set the passed updated_at value")

    def test_str(self):
        """
        Test for checking the string representation of BaseModel
        """
        id = '219c8141-85ca-4f00-923b-5a3b47fc2517'
        tc = '2023-05-11T21:53:37.103600'
        tu = '2023-05-11T21:53:37.103650'
        b = BaseModel(id=id, created_at=tc, updated_at=tu)
        b.name = 'TestInstance'

        self.assertEqual(
            b.__str__(), "[BaseModel] ({}) {}".format(id, b.__dict__),
            "string representation should output [Class] (id) dict")

    def test_save(self):
        """
        Test for checking save function setting update_at
        """
        id = '219c8141-85ca-4f00-923b-5a3b47fc2517'
        tc = '2023-05-11T21:53:37.103600'
        tu = '2023-05-11T21:53:37.103650'
        b = BaseModel(id=id, created_at=tc, updated_at=tu)
        c1 = datetime.now()
        b.save()
        c2 = datetime.now()

        self.assertGreaterEqual(
            (b.updated_at - c1) / timedelta(milliseconds=1), 0,
            "initializer should set updated_at appropriately")
        self.assertGreaterEqual(
            (c2 - b.updated_at) / timedelta(milliseconds=1), 0,
            "initializer should set updated_at appropriately")

    def test_to_dict(self):
        """
        Test for checking conversion of BaseModel to dict
        """
        id = '219c8141-85ca-4f00-923b-5a3b47fc2517'
        tc = '2023-05-11T21:53:37.103600'
        tu = '2023-05-11T21:53:37.103650'
        b = BaseModel(id=id, created_at=tc, updated_at=tu)
        b.name = 'TestInstance'
        d = {
            '__class__': 'BaseModel',
            'id': id,
            'created_at': tc,
            'updated_at': tu,
            'name': 'TestInstance'
        }

        self.assertDictEqual(
            b.to_dict(), d,
            "dict representation output is incorrect")
