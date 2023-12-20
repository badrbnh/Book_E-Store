#!/usr/bin/python3

from models.user import User

class Admin(User):
    """It defines an admin user that have higher permission than customers"""
    is_admin = bool
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    