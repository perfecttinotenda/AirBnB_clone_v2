#!/usr/bin/python3
"""Tests for console
   Code adjusted to fit prev class names & Def
"""

import unittest
import console
from console import HBNBCommand


class test_console(unittest.TestCase):
    """class_test console"""

    def create(self):
        """create_instance"""
        return HBNBCommand()

    def test_quit(self):
        """ test method to quit
        """
        con = self.create()
        self.assertTrue(con.onecmd("quit"))

    def test_EOF(self):
        """test method EQF
        """
        con = self.create()
        self.assertTrue(con.onecmd("EOF"))