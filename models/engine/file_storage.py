#!/usr/bin/python3

import json
import os.path
from models.base_model import BaseModel


class FileStorage():
    __file_path = "file_store.json"
    __objects = {}

    def all(self):
        return self.__objects
    
    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        save = {}
        for key, val in self.__objects.items():
            save[key] = val.to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(save, f)

    def reload(self):
        if os.path.isfile(self.__file_path):
            with open(self.__file_path) as f:
                save = json.load(f)
            for key, val in save.items():
                print(val)
                BaseModel(val)
