#!/usr/bin/python3
"""The Author Class"""
from models.basemodel import BaseModel


class Author(BaseModel):
    """class building"""
    author_name = ""
    description = ""
    bio = ""
    coutry = ""

    def __init__(self, *args, **kwags):
        super().__init__(*args, **kwags)
