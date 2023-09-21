#!/usr/bin/python3
"""Base model class for AirBnB clone"""

from datetime import datetime
import models
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime, ForeignKey
from uuid import uuid4

Base = declarative_base()


class BaseModel:
    """Base class for all models in AirBnB clone"""

    id = Column(String(60), primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Initialize BaseModel from kwargs"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Return string representation"""
        return "[{}] ({}) {}".format(
            (str(type(self)).split('.')[-1])
            .split('\'')[0], self.id, self.__dict__)

    def save(self):
        """Update updated_at time on change"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert to dictionary"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__': (str(type(self))
                                         .split('.')[-1]).split('\'')[0]})
        if "_sa_instance_state" in dictionary.keys():
            del dictionary["_sa_instance_state"]
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary

    def delete(self):
        """Delete instance"""
        models.storage.delete()
