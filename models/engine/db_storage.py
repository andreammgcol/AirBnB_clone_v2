#!/usr/bin/python3
"""this is the database engine"""
import sqlalchemy
import os

class DBStorage():
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
