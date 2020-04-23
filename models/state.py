#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship, backref
import os
import models
from models.city import City


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = "states"

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", passive_deletes=True, backref="state")
    else:
        name = ""


        @property
        def cities(self):
            """ list of cities """
            cities_list = []
            cities = models.storage.all(city)
            for city in cities.values():
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list
