#!/usr/bin/python3
"""This file contains the FileStorage class"""

import json
import os

class FileStorage:
    """ this is the class """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects """
        return (FileStorage.__objects)
    def new(self, obj):
        """  sets in __objects the obj with key <obj class name>.id """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj
    def save(self):
        with open(FileStorage.__file_path, "w", encoding="utf-8") as jsonfile:
            temp_dict = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(temp_dict, jsonfile)
    def reload(self):
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as jsonfile:
            tempdict = json.load(jsonfile)
            tempdict = {k: self.classes()[v["__class__"]](**v)
                        for k, v in tempdict.items()}
            FileStorage.__objects = tempdict
    def classes(self):
        """Returns a dictionary of valid classes and their references."""
        from models.base_model import BaseModel

        classes = {"BaseModel": BaseModel}
        return classes
