#!/usr/bin/python3
"""Test ye console"""

import unittest
import console
from console import HBNBCommand


class test_console(unittest.TestCase):
    """class ye console"""

    def create(self):
        """creat3 intance"""
        return HBNBCommand()

    def test_quit(self):
        """ test ye method quit
        """
        con = self.create()
        self.assertTrue(con.onecmd("quit"))

    def test_EOF(self):
        """test ye method EQF
        """
        con = self.create()
        self.assertTrue(con.onecmd("EOF"))
