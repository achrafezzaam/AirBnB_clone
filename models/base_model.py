#!/usr/bin/python3

import uuid
from datetime import datetime
import models

class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
            if 'created_at' in kwargs:
                self.created_at = datetime.strptime(kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
            if 'updated_at' in kwargs:
                self.updated_at = datetime.strptime(kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                       self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        info_dict = {"__class__": self.__class__.__name__}
        for key, val in self.__dict__.items():
            if type(val) is datetime:
               info_dict[key] = val.isoformat("T") 
            else:
                info_dict[key] = val
        return info_dict
