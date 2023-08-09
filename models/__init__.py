#!/usr/bin/python3
''' Create the storage where the created object will be saved
    for later re-use (for now the data is stored in a JSON file)'''
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
