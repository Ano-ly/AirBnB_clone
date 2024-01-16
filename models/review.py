#!/usr/bin/python3
"""Module for review class."""

from models.base_model import BaseModel


class Review(BaseModel):
    """ class that represents reviews """

    place_id = ""
    user_id = ""
    text = ""
