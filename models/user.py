#!/usr/bin/python3
'''A class user that inherent from BaseModel'''
from models.base_model import BaseModel


class User(BaseModel):
    """ This represents class User"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
