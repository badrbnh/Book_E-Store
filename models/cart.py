#!/usr/bin/python3
"""The Cart Class"""
from models.basemodel import BaseModel
from models.orders import Orders


class Cart(Orders):
    """class building"""
    order = ""
    total = 0.0

    def __init__(self, *args, **kwags):
        super().__init__(*args, **kwags)
