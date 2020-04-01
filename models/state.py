#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from os import getenv
from os import environ
from models import storage, City


class State(BaseModel):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship(
        "City", cascade="all, delete",
        backref=backref("state", cascade="all, delete"))
    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """ list of cities"""
            cities_list = [
                value for key, value in storage.all(City).items()
                if value.state_id == self.id]
            return cities_list
