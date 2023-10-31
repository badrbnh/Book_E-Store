#!/usr/bin/pyhton3
""" FileStorage class """

from models.basemodel import BaseModel
import json

class FileStorage():
    __file_path = "file.json"
    __objects = {}
    
    def all(self):
        return self.__objects
        
    def new (self, obj):
        if obj is not None:
            key = obj.__class__.__name__ + '.' + obj.id
            self.__objects[key] = obj

    def save(self):
        dict = {key : value.to_dict() for key, value in self.__objects.items()}
        
        with open(self.__file_path, "w", encoding='utf-8') as file:
            json.dump(dict, file, indent=4)
    
        
    
