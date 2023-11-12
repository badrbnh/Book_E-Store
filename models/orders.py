#!/usr/bin/python3
"""The Orders Class"""
from models.basemodel import BaseModel
from models.customer import Customer


class Orders(Customer):
    """class building"""
    price = 0.0
    quantity = ""

    def __init__(self, *args, **kwags):
        super().__init__(*args, **kwags)
