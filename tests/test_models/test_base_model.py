#!/usr/bin/python3

"""
    All test for the base_model will be implemented here.
"""

import unittest
from models.base_model import BaseModel
from io import StringIO
import sys
import datetime


class TestBase(unittest.TestCase):
    """
        Test base class_model.
    """

    def setUp(self):
        """
            Initialize_instance.
        """
        self.my_model = BaseModel()
        self.my_model.name = "Binita Rai"

    def TearDown(self):
        """
            Removing instance.
        """
        del self.my_model

    def test_id_type(self):
        """
            Check the type of the i_d is a str.
        """
        self.assertEqual("<class 'str'>", str(type(self.my_model.id)))

    def test_ids_differ(self):
        """
            Checks that the i_ds btwn two instances wil be different.
        """
        new_model = BaseModel()
        self.assertNotEqual(new_model.id, self.my_model.id)

    def test_name(self):
        """
            Checks that an attr can be added.
        """
        self.assertEqual("Binita Rai", self.my_model.name)

    def test_a_updated_created_equal(self):
        """
            Checks that both dates will be an equal.
        """
        self.assertEqual(self.my_model.updated_at.year,
                         self.my_model.created_at.year)

    def test_save(self):
        """
            Checks aftr updating that instance; the dates diff in the
            updated_at attr.
        """
        old_update = self.my_model.updated_at
        self.my_model.save()
        self.assertNotEqual(self.my_model.updated_at, old_update)

    def test_str_overide(self):
        """
            Checks the right message will be printed.
        """
        backup = sys.stdout
        inst_id = self.my_model.id
        capture_out = StringIO()
        sys.stdout = capture_out
        print(self.my_model)

        cap = capture_out.getvalue().split(" ")
        self.assertEqual(cap[0], "[BaseModel]")

        self.assertEqual(cap[1], "({})".format(inst_id))
        sys.stdout = backup

    def test_to_dict_type(self):
        """
            Check the to_dict method return type.
        """

        self.assertEqual("<class 'dict'>",
                         str(type(self.my_model.to_dict())))

    def test_to_dict_class(self):
        """
            Check that __class__ key exts.
        """

        self.assertEqual("BaseModel", (self.my_model.to_dict())["__class__"])

    def test_to_dict_type_updated_at(self):
        """
            Check type of the val of updated_at.
        """
        self.assertEqual("<class 'str'>",
                         str(type((self.my_model.to_dict())["updated_at"])))

    def test_to_dict_type_created_at(self):
        """
            Check type of val of created_at.
        """
        tmp = self.my_model.to_dict()
        self.assertEqual("<class 'str'>", str(type(tmp["created_at"])))

    def test_kwargs_instantiation(self):
        """
            Test an instance is created using the
            key val_pair.
        """
        my_model_dict = self.my_model.to_dict()
        new_model = BaseModel(**my_model_dict)
        self.assertEqual(new_model.id, self.my_model.id)

    def test_type_created_at(self):
        """
            Test the new_model's updated_at
            data_type is datetime.
        """
        my_model_dict = self.my_model.to_dict()
        new_model = BaseModel(my_model_dict)
        self.assertTrue(isinstance(new_model.created_at, datetime.datetime))

    def test_type_updated_at(self):
        """
            Test the new_model's created_at
            data_type is datetime.
        """
        my_model_dict = self.my_model.to_dict()
        new_model = BaseModel(my_model_dict)
        self.assertTrue(isinstance(new_model.updated_at, datetime.datetime))

    def test_compare_dict(self):
        """
            Test the new_model's & my_model's
            dictionary val are all the same.
        """
        my_model_dict = self.my_model.to_dict()
        new_model = BaseModel(**my_model_dict)
        new_model_dict = new_model.to_dict()
        self.assertEqual(my_model_dict, new_model_dict)