#!/usr/bin/python3

import uuid
from datetime import datetime


class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return "[{}] ({}) <{}>".format(self.__class__.__name__,
                                       self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        info_dict = {"__class__": self.__class__.__name__}
        for key, val in self.__dict__.items():
            if type(val) is datetime:
               info_dict[key] = val.isoformat("T") 
            else:
                info_dict[key] = val
        return info_dict
