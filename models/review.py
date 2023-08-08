#!/usr/bin/python3
''' Define the Review class '''
from base_model import BaseModel


class Review(BaseModel):
    ''' Create a Review object '''
    place_id = ""
    user_id = ""
    text = ""
