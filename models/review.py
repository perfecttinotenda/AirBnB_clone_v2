#!/usr/bin/python3
'''class inherent ye BaseModel'''
from models.base_model import BaseModel


class Review(BaseModel):
    """The class Review"""

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """initializing Review"""
        super().__init__(*args, **kwargs)
