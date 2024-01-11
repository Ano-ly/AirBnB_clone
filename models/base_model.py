#!/usr/bin/python3
"""This file contains the BaseModel class"""

import uuid
from datetime import datetime, date


class BaseModel:
    """This is the BaseModel class"""

    def __init__(self):
        """Initialises instance"""

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Overwrites __str__ method"""

        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id,
                self.__dict__))

    def save(self):
        """Updates updated_at attribute with current time"""

        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns the dictionary representation of the instance"""

        ret_dict = {}
        for key, value in (self.__dict__).items():
            ret_dict.update({key: value})
        ret_dict.update({"__class__": "{}".format(self.__class__.__name__)})
        ret_dict["created_at"] = datetime.isoformat(self.created_at)
        ret_dict["updated_at"] = datetime.isoformat(self.updated_at)
        return (ret_dict)
