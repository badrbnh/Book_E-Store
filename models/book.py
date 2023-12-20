#!/usr/bin/python3
"""The Book Class"""
from models.basemodel import BaseModel
from models.author import Author


class Book(Author):
    """class building"""
    title = ""
    genre = ""
    description = ""
    price = 0.0

    def __init__(self, *args, **kwags):
        super().__init__(*args, **kwags)

