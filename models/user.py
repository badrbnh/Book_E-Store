#!/usr/bin/python3
"""The User Class"""
import models
from models.basemodel import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from hashlib import md5


class User(BaseModel):
    """Representation of a user """
    if models.storage_t == 'db':
        __tablename__ = 'users'
        user_name = Column(String(128), nullable=False)
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        pnumber = Column(String(128), nullable=False)
        country = Column(String(128), nullable=False)
    else:
        user_name = ""
        email = ""
        password = ""
        pnumber = 0
        country = ""

    def __init__(self, *args, **kwags):
        super().__init__(*args, **kwags)
