#!/usr/bin/python3

from models.basemodel import BaseModel

class Author(BaseModel):
    author_name = ""
    bio = ""
    description = ""
    country = ""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)