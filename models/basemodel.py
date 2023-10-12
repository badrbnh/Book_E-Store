#!/usr/bin/python3
"""This is the base model of ouer classes"""

from datetime import *
from uuid import uuid4

class BaseModel():
    """Base class of the models"""
    
    def __init__(self, *args, **kwargs):
        """Constructor of the attributes"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%d-%H:%M:%S")
                if key != "__class__":
                    setattr(self, key, value)
        self.id = str(uuid4())
        self.created_at = self.updated_at = datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
    
    def __str__(self):
        """returns the representation of the class model"""
        return f"[{self.__class__.__name__}] {(self.id)} {self.__dict__}"
    
    def save(self):
        """method that update the time whenever save"""
     
        self.updated_at = datetime.now().strftime("%Y-%m-%d-%H:%M:%S")

    def to_dict(self):
        """turns objects to directory"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at
        new_dict["updated_at"] = self.updated_at
        return new_dict
