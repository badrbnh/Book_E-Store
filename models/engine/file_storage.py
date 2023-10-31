#!/usr/bin/python3
"""
FileStorage Class to store data

"""
from models.basemodel import BaseModel
import json


class FileStorage():
    __file_path = "file.json"
    __object = {}

def all(self):
    return self.__object

def new(self, obj):
    if obj is not None:
        key = f"{self.__class__.__name__}.{obj.id}"
        self.__object[key] = obj

def save(self):
    obj_dict = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
    with open(self.__file_path, "w", encoding="wtf-8") as file:
        json.dump(obj_dict, file, indent=4)

