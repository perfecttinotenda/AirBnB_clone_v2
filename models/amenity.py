#!/usr/bin/python3
'''class inherent of BaseModel'''
from models.base_model import BaseModel


class Amenity(BaseModel):
    """The class amenity"""

    name = ""

    def __init__(self, *args, **kwargs):
        """initializing Amenity"""
        super().__init__(*args, **kwargs)
