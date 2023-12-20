#!/usr/bin/python3
"""database storage for e-book store"""

from models.basemodel import BaseModel, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
import models
from models.user import User
from models.admin import Admin
from models.author import Author
from models.book import Book
from models.cart import Cart
from models.customer import Customer
from models.orders import Orders

classes = {"User": User, "Admin": Admin, "Author": Author, "Book": Book, "Customer": Customer, "Orders": Orders,
           "Cart": Cart}
class DBStorage():
    """database storage for e-book store"""
    __engine = None
    __session = None
    
    def __init__(self):
        """initializes DBStorage"""
        user = getenv("EBOOK_MYSQL_USER")
        pwd = getenv("EBOOK_MYSQL_PWD")
        host = getenv("EBOOK_MYSQL_HOST")

        if getenv("EBOOK_ENV") == "test":
            Base.metadata.drop_all(self.__engine)
        
    def all(self, cls=None):
        """Retrieve all objects in chosen class or all classes if not specified"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is clss or classes[clss] is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return new_dict
    
    def new(self, obj):
        """adding the obj to the current session"""
        self.__session.add(obj)
    
    def save(self):
        """save the current database session"""
        self.__session.commit()
        
    def delete(self, obj):
        """delete the obj from the current database session"""
        if obj is not None:
            self.__session.delete(obj)
    
    def reload(self):
        """reload data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session
            
    def close(self):
        """call remove on the private session"""
        self.__session.remove()
    
    def get(self, cls, id):
        """Retreive an class object of a specified id"""
        if cls not in classes.values():
            return None
        
        all_cls = models.storage.all()
        for value in all_cls.values():
            if value.id == id:
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
