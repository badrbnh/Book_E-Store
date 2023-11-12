#!/usr/bin/python3
"""
FileStorage Class to store data

"""
from models.basemodel import BaseModel
import json
import os


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

def reload(self):
        """loads string repr of objects from json file"""
        json_file = FileStorage.__file_path
        if os.path.exists(json_file):
            with open(json_file, "r") as file:
                obj_dict = json.load(file)
                for obj in obj_dict.values():
                    name = obj["__class__"]
                    self.new(globals()[name](**obj))

def clear(self):
        """clears the dictionary of objects"""
        keys_to_delete = list(FileStorage.__objects.keys())
        for k in keys_to_delete:
            del FileStorage.__objects[k]
        json_files = [file for file in os.listdir(os.getcwd())
                      if file.endswith(".json")]
        if not json_files:
            return
        for file in json_files:
            file_path = os.path.join(os.getcwd(), file)
            try:
                os.remove(file_path)
            except OSError as e:
                print(f"Error removing {file}: {e}")
