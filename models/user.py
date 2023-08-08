#!/usr/bin/python3
''' Define the User class '''
from models.base_model import BaseModel


class User(BaseModel):
    ''' Create a User object '''
    email = ""
    password = ""
    first_name = ""
    last_name = ""
