#!/usr/bin/python3
"""The Base Model Of Console"""
from datetime import datetime
from uuid import uuid4
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class BaseModel():
    """Class that is the is base"""
    def __init__(self, *args, **kwags):
        """constructor of the base model class"""
        if kwags:
            for key, value in kwags.items():
                    if key == "created_at" or key == "updated_at":
                        value = datetime.strptime(value, "%Y-%m-%d-%H-%M-%S")
                    if key != "__class__":
                        setattr(self, key, value)
        self.id = str(uuid4())
        self.created_at = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        self.updated_at = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
            

    def __str__(self):
        """represente the dictinory with the class name"""
        return f"{__class__.__name__} {(self.id)} {self.__dict__}"
    
    def save(self):
        """save update_at attribute """
        self.updated_at = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

    def to_dict(self):
        """trnnsform all instance into a dictionary format"""
        dict = self.__dict__.copy()
        dict["__class__"] = self.__class__.__name__
        dict["created_at"] = self.created_at
        dict["updated_at"] = self.updated_at
        return dict
