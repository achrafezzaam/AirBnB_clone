#!/usr/bin/python3
''' Define the BaseModel class that will be inherited by the User, Place,
    State, Review, City and Amenity classes '''
import uuid
from datetime import datetime
import models


class BaseModel:
    ''' Create a BaseModel object '''
    instances = {}

    def __init__(self, *args, **kwargs):
        ''' Instantiate the BaseModel object

        Args:
            args (None):    not used
            kwargs (dict):  key/value paires used to instantiate
                            a BaseModel object
        '''
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
            if 'created_at' in kwargs:
                self.created_at = datetime.strptime(kwargs['created_at'],
                                                    '%Y-%m-%dT%H:%M:%S.%f')
            if 'updated_at' in kwargs:
                self.updated_at = datetime.strptime(kwargs['updated_at'],
                                                    '%Y-%m-%dT%H:%M:%S.%f')
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()


    @classmethod
    def create(cls, *args, **kwargs):
        instance = cls(*args, **kwargs)
        cls.instances[instance.id] = instance

        return instance

    def __str__(self):
        ''' Format of the instance when printed '''
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        ''' Save the object in the storage (a JSON file for now) '''
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        ''' Turn the object to a dictionary '''
        info_dict = {"__class__": self.__class__.__name__}
        for key, val in self.__dict__.items():
            if type(val) is datetime:
                info_dict[key] = val.isoformat("T")
            else:
                info_dict[key] = val
        return info_dict
