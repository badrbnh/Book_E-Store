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
from os import getenv


class DBstorage():
    __engine = None
    __seesion = None

    def __init__(self):
        user = getenv("EBOOK_MYSQL_USER")
        password = getenv("EBOOK_MYSQL_PWD")
        host = getenv("EBOOK_MYSQL_HOST")
        database = getenv("EBOOk_MYSQL_DB")
        self.engine = create_engine("mysql+mysqldb://{}{}@{}/{}"
                               .format(user, password, host, database))
        if getenv("EBOOK_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

