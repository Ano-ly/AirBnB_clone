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
            tempdict = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(tempdict, jsonfile)
    def reload(self):
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as jsonfile:
            tempdict = json.load(f)
            FileStorage.__objects = tempdict

