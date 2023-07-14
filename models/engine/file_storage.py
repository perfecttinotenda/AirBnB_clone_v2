#!/usr/bin/python3
"""
    Define_class with the FileStorage_Module
"""
import json
import models


class FileStorage:
    """
        Serializes instances to JSON_file & deserializes to JSON_file again.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
            RET the dict
        """
        return self.__objects

    def new(self, obj):
        """
        Set new_object into __objects
        """
        key = str(obj.__class__.__name__) + "." + str(obj.id)
        value_dict = obj
        FileStorage.__objects[key] = value_dict

    def save(self):
        """
        Serializes objects to a JSON_file
        """
        objects_dict = {}
        for key, val in FileStorage.__objects.items():
            objects_dict[key] = val.to_dict()

        with open(FileStorage.__file_path, mode='w', encoding="UTF8") as fd:
            json.dump(objects_dict, fd)

    def reload(self):
        """
        Reloads file & deserializes JSON_file into __objects
        """

        try:
            with open(FileStorage.__file_path, encoding="UTF8") as fd:
                FileStorage.__objects = json.load(fd)
            for key, val in FileStorage.__objects.items():
                class_name = val["__class__"]
                class_name = models.classes[class_name]
                FileStorage.__objects[key] = class_name(**val)
        except FileNotFoundError:
            pass