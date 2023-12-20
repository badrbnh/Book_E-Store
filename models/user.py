#!/usr/bin/python3
from models.basemodel import BaseModel

class User(BaseModel):
    username = ""
    email = ""
    pnumber = 0
    country = ""
    password = ""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    