#!/usr/bin/python3

from models.customer import Customer

class Orders(Customer):
    price = 0.0
    quantity = 0
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
