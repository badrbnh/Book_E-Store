"""
initialize the models package
"""

from os import getenv


storage_t = getenv("EBOOK_TYPE_STORAGE")

if storage_t == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.filestorage import FileStorage
    storage = FileStorage()
storage.reload()