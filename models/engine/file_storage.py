#!/usr/bin/python3

import json


class FileStorage():
    __file_path = "file_store.json"
    __objects = {}

    def all(self):
        return self.__objects
    
    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        json.dump(__objects, __file_path)

    def reload(self):
        with open(__file_path) as f:
            __objects.update(json.dump(f))
