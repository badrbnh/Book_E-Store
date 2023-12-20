#!/usr/bin/pyhton3
""" FileStorage class """

from models.basemodel import BaseModel
import json
from models.author import Author
from models.book import Book
from models.customer import Customer
from models.orders import Orders
from models.cart import Cart
from models.user import User
from models.admin import Admin
import models

classes = {"User": User, "Admin": Admin, "Author": Author, "Book": Book, "Customer": Customer, "Orders": Orders,
           "Cart": Cart}

class FileStorage():
    __file_path = "file.json"
    __objects = {}
    
    def all(self, cls=None):
        """returns the dictionary __objects"""
        if cls is not None:
            new_dict = {}
            for key, value in self.__objects.items():
                if cls == value.__class__ or cls == value.__class__.__name__:
                    new_dict[key] = value
            return new_dict
        return self.__objects
        
    def new (self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj is not None:
            key = obj.__class__.__name__ + '.' + obj.id
            self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        json_objects = {}
        for key in self.__objects:
            if key == "password":
                json_objects[key].decode()
            json_objects[key] = self.__objects[key].to_dict(save_fs=1)
        with open(self.__file_path, 'w') as f:
            json.dump(json_objects, f)

    def reload(self):
        """loads dictionary from file"""
        try:
            with open(self.__file_path, "r", encoding="utf-8") as fl:
                for obj in json.load(fl).values():
                    name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(name)(**obj))
        except FileNotFoundError:
            pass
    
    def delete(self, obj=None):
        """checks if an object exists and delets it"""
        try:
            del self.__objects["{}.{}".format(type(obj).__name__, obj.id)]
        except (AttributeError, KeyError):
            pass

    def close(self):
        """ deserializing the JSON file to objects """
        self.reload()
    
    def get(self, cls, id):
        """
        Returns the object based on the class name and its ID, or
        None if not found
        """
        if cls not in classes.values():
            return None

        all_cls = models.storage.all(cls)
        for value in all_cls.values():
            if (value.id == id):
                return value

        return None

    def count(self, cls=None):
        """
        count the number of objects in storage
        """
        all_class = classes.values()

        if not cls:
            count = 0
            for clas in all_class:
                count += len(models.storage.all(clas).values())
        else:
            count = len(models.storage.all(cls).values())

        return count
