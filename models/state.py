#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from os import getenv
from os import environ
import models
from models.city import City


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    cities = relationship(
        "City", cascade="all, delete, delete-orphan",
        backref=backref("state", cascade="all,delete"),
        passive_deletes=True,
        single_parent=True)

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """ list of cities """
            cities_list = []
            for key, value in models.storage.__objects.items():
                if "City" == value[__class__] and self.id == value[state_id]:
                    cities_list.append(value)
            return cities_list
