#!/usr/bin/python3

"""
    test_amenity model.
"""

import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
        Test Amenity_class
    """

    def test_Amenity_inheritence(self):
        """
            test_Amenity_class Inherits from BaseModel
        """        
        new_amenity = Amenity()
        self.assertIsInstance(new_amenity, BaseModel)

    def test_Amenity_attributes(self):
        """
            Test_Amenity_class had name_attr.
        """
        new_amenity = Amenity()
        self.assertTrue("name" in new_amenity.__dir__())

    def test_Amenity_attribute_type(self):
        """
            Test_Amenity_class had name attr_type.
        """
        new_amenity = Amenity()
        name_value = getattr(new_amenity, "name")
        self.assertIsInstance(name_value, str)