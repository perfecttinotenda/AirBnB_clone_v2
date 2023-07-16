#!/usr/bin/python3
"""class inherent ye BaseModel"""
from models.base_model import BaseModel


class State(BaseModel):
    """The class State"""

    name = ""

    def __init__(self, *args, **kwargs):
        """initializing State"""
        super().__init__(*args, **kwargs)
