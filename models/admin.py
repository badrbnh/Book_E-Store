#!/usr/bin/python3
"""The Admin Class"""
from models.basemodel import BaseModel
from models.user import User

class Admin(User):
    """class building"""
    is_admin = bool

    def __init__(self, *args, **kwags):
        super().__init__(*args, **kwags)