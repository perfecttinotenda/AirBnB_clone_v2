#!/usr/bin/python3
"""create a unique FileStorage instance formy application"""
from models.engine.file_storage import FileStorage

"""A var storage, an instance of FileStorage"""
storage = FileStorage()
storage.reload()
