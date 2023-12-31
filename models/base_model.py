#!/usr/bin/env python3
"""A module that defines the BaseModel Class"""
import uuid
from datetime import datetime
from models import storage


class BaseModel():
    """The baseModel class"""

    def __init__(self, *args, **kwargs):
        """Initialization function"""
        if (kwargs is None or len(kwargs) == 0):
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            self.id = kwargs.get("id", str(uuid.uuid4()))
            for (key, value) in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.fromisoformat(value))
                elif key != "__class__":
                    setattr(self, key, value)

    def __str__(self):
        """custom str function"""
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        "updates 'updated_at' with current datetime"
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__"""
        result = {}
        for (key, value) in self.__dict__.items():
            if (key == "created_at" or key == "updated_at"):
                value = value.isoformat()
            result[key] = value
            result["__class__"] = self.__class__.__name__
        return result
