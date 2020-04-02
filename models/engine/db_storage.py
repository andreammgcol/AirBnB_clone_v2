#!/usr/bin/python3
"""this is the database engine"""
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, create_engine
from sqlalchemy.orm import relationship, backref
import os
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """this class is the db engine"""
    __engine = None
    __session = None

    def __init__(self):
        """initialice the dbs"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            os.environ.get("HBNB_MYSQL_USER"),
            os.environ.get("HBNB_MYSQL_PWD"),
            os.environ.get("HBNB_MYSQL_HOST"),
            os.environ.get("HBNB_MYSQL_DB")),
            pool_pre_ping=True)
        if os.environ.get("HBNB_ENV") == 'test':
            Base.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """return a dictionary of objects"""
        le_dict = {}
        if cls:
            for row in self.__session.query(cls.__name__):
                key = "{}.{}".format(cls.__name__, row.id)
                le_dict[key] = row
        else:
            for le_cls in Base.metadata.tables.keys():
                for row in self.__session.query(le_cls):
                    key = "{}.{}".format(le_cls, row.id)
                    le_dict[key] = row

        return le_dict

    def new(self, obj):
        """add the object to the session"""
        self.__session.add(obj)

    def save(self):
        """commit"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete"""
        if obj:
            self.__session.delete(obj.id)

    def reload(self):
        """reload"""
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(
            self.__engine,
            expire_on_commit=False))
