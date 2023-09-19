#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel):
    """ State class """
    __tablename__ = 'states'  # Specify the table name
    name = Column(String(128), nullable=False)

    # For DBStorage, create a relationship with City
    cities = relationship(
        "City",
        backref="state",
        cascade="all, delete-orphan")
