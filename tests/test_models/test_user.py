#!/usr/bin/python3
"""
This "test_user.py" module defines one class:
    TestUser: for testing the functionality of the User class

Run from project directory using:
$   python3 -m unittest ./tests/test_models/test_user.py
"""
import unittest

from models.user import User


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
        Test for checking the creation of User
        """
        u1 = User()
        u1.email = "testuser@email.com"
        u1.password = "0123456789"
        u1.first_name = "Test"
        u1.last_name = "User"
        u1.save()
        u2 = User(
            id='219c8141-85ca-4f00-923b-5a3b47fc2517',
            created_at='2023-05-11T21:53:37.103600',
            updated_at='2023-05-11T21:53:37.103650',
            email='nextuser@email.com',
            password='9876543210',
            first_name='Next',
            last_name='User')

        self.assertEqual(
            type(u1), User,
            "initializer should return a User")
        self.assertEqual(
            u1.email, "testuser@email.com",
            "initializer should set the correct passed value")
        self.assertEqual(
            u1.password, "0123456789",
            "initializer should set the correct passed value")
        self.assertEqual(
            u1.first_name, "Test",
            "initializer should set the correct passed value")
        self.assertEqual(
            u1.last_name, "User",
            "initializer should set the correct passed value")
        self.assertEqual(
            u2.id, "219c8141-85ca-4f00-923b-5a3b47fc2517",
            "initializer should set the correct passed value")
        self.assertEqual(
            u2.email, "nextuser@email.com",
            "initializer should set the correct passed value")
        self.assertEqual(
            u2.password, "9876543210",
            "initializer should set the correct passed value")
        self.assertEqual(
            u2.first_name, "Next",
            "initializer should set the correct passed value")
        self.assertEqual(
            u2.last_name, "User",
            "initializer should set the correct passed value")
