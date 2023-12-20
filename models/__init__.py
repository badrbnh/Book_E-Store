#!/usr/bin/python3
"""
initialize the models package
"""
from os import getenv
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage


storage_t = getenv("EBOOK_TYPE_STORAGE")

if storage_t == "db":
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()
