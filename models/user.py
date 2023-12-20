#!/usr/bin/python3
"""The User Class"""
from models.basemodel import BaseModel


class User(BaseModel):
    """class building"""
    user_name = ""
    email = ""
    password = ""
    pnumber = 0
    country = ""

    def __init__(self, *args, **kwags):
        super().__init__(*args, **kwags)
