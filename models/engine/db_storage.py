#!/usr/bin/python3
"""
DBstorage Class to store data

"""
import models
from models.user import User
from models.admin import Admin
from models.author import Author
from models.book import Book
from models.cart import Cart
from models.customer import Customer
from models.orders import Orders
from models.basemodel import BaseModel, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv

classes = {"User": User, "Admin": Admin, "Author": Author, "Book": Book, "Customer": Customer, "Orders": Orders,
           "Cart": Cart}

class DBstorage():
    __engine = None
    __seesion = None

    def __init__(self):
        user = getenv("EBOOK_MYSQL_USER")
        password = getenv("EBOOK_MYSQL_PWD")
        host = getenv("EBOOK_MYSQL_HOST")
        database = getenv("EBOOk_MYSQL_DB")
        self.engine = create_engine("postgresql+psycopg2://{}{}@{}/{}"
                               .format(user, password, host, database))
        if getenv("EBOOK_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__seesion.query(classes[clss].all())
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return new_dict

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__seesion = Session

    def get(self, cls, id):
        """Retrieve a object"""

        if cls and id:
            objs = self.all(cls)
            key = f'{cls.__name__}.{id}'
            return objs.get(key)
        return None
    
    def count(self, cls=None):
        """count the number of objects in storage"""
        if cls is None:
            return len(self.all())
        else:
            return len(self.all(cls))

