#!/usr/bin/python3

from models.orders import Orders

class Cart(Orders):
    order = ""
    total = 0.0
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)