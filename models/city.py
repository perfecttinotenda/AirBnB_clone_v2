#!/usr/bin/python3
"""class inherent ye BaseModel"""
from models.base_model import BaseModel


class City(BaseModel):
    """The class city"""

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """initializing City"""
        super().__init__(*args, **kwargs)
