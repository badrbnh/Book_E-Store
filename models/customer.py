#!/usr/bin/python3
from models.basemodel import BaseModel
from models.user import User

class Customer(User):
    """user that has lower permissions than admin"""
    address = ""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
