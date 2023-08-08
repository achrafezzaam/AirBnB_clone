#!/usr/bin/python3
''' Define the FileStorage class '''
import json
import os.path
from models.base_model import BaseModel


class FileStorage():
    ''' Create the FileStorage object '''
    __file_path = "file_store.json"
    __objects = {}

    def all(self):
        ''' Return all the stored objects '''
        return self.__objects

    def new(self, obj):
        ''' Add a new object to the objects dict

        Args:
            obj (BaseModel):    The object to save
        '''
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        ''' Serializes the objects attribute value to JSON
            and saves it to the file_path file'''
        save = {}
        for key, val in self.__objects.items():
            save[key] = val.to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(save, f)

    def reload(self):
        ''' Deserialize the file_path content and add the
            stored values to the objects attribute '''
        if os.path.isfile(self.__file_path):
            with open(self.__file_path) as f:
                save = json.load(f)
            for key, val in save.items():
                print(val)
                BaseModel(val)
