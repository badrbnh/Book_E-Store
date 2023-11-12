#!/usr/bin/python3
"""The User Class"""
from models.basemodel import BaseModel
from models.user import User

class Customer(User):
    """class building"""
    address = ""

    def __init__(self, *args, **kwags):
        super().__init__(*args, **kwags)