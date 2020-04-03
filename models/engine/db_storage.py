#!/usr/bin/python3
"""this is the database engine"""
from sqlalchemy import create_engine, MetaData
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship, backref, scoped_session, sessionmaker
import os
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """this class is the db engine
    Attributes:
        __file_path: path to the JSON file
        __objects: objects will be stored
    """
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
        """return a dictionary of objects
        Return:
            returns a dictionary of __object
        """
        le_dict = {}
        if cls:
            for row in self.__session.query(cls.__name__):
                key = "{}.{}".format(cls.__name__, row.id)
                le_dict[key] = row
        else:
            for le_cls in [State, User, Place, City, Review]:
                for row in self.__session.query(le_cls):
                    key = "{}.{}".format(row.__class__.__name__, row.id)
                    le_dict[key] = row
        if "_sa_instance_state" in le_dict:
            del le_dict["_sa_instance_state"]

        return le_dict

    def new(self, obj):
        """add the object to the session
        Args:
            obj: given object
        """
        self.__session.add(obj)
        self.save()

    def save(self):
        """commit"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete
        Args:
            obj: given object
        """
        if obj:
            self.__session.delete(obj.id)
            self.save()

    def reload(self):
        """reload"""
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(
            self.__engine,
            expire_on_commit=False))
