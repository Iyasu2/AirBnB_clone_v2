#!/usr/bin/python3
"""Initialize the models package"""
from os import getenv

# Check the value of HBNB_TYPE_STORAGE environment variable
HBNB_TYPE_STORAGE = getenv('HBNB_TYPE_STORAGE')

if HBNB_TYPE_STORAGE == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()
elif HBNB_TYPE_STORAGE == 'file':
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()
else:
    raise ValueError("Invalid HBNB_TYPE_STORAGE value. Use 'db' or 'file'.")
