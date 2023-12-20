#!/usr/bin/python3

from models.author import Author

class Book(Author):
    title = ""
    description = ""
    country = ""
    genre = ""
    price = 0.0
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)