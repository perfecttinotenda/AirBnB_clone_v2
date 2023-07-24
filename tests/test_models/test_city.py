#!/usr/bin/python3
"""Module yema test City class"""
import unittest
import json
import pep8
import datetime

from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Test City class yeimplementation yacho"""
    def test_doc_module(self):
        """Module documentation redu"""
        doc = City.__doc__
        self.assertGreater(len(doc), 1)

    def test_pep8_conformance_city(self):
        """Test that models/city.py will/or conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_city(self):
        """Test that tests/test_models/test_city.py will/or conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        res = pep8style.check_files(['tests/test_models/test_city.py'])
        self.assertEqual(res.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_doc_constructor(self):
        """Constructor yedocumentation redu"""
        doc = City.__init__.__doc__
        self.assertGreater(len(doc), 1)

    def test_class(self):
        """Validate yema types of the attr an class"""
        with self.subTest(msg='Inheritance'):
            self.assertTrue(issubclass(City, BaseModel))

        with self.subTest(msg='Attributes'):
            self.assertIsInstance(City.name, str)
            self.assertIsInstance(City.state_id, str)


if __name__ == '__main__':
    unittest.main()
