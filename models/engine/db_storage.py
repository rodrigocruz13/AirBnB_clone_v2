#!/usr/bin/python3
"""This is the Database storage class for AirBnB"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from os import getenv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String
from sqlalchemy import (create_engine)


class DBStorage:
    """This class serializes instances to a JSON file and
    deserializes JSON file to instances
    Attributes:
        __file_path: path to the JSON file
        __objects: objects will be stored
    """
    __engine = None
    __session = None

    def __init__(self):
        ''' Comentario cool '''
        env_user=getenv('HBNB_MYSQL_USER')
        env_passwd=getenv('HBNB_MYSQL_PWD')
        env_host=getenv('HBNB_MYSQL_HOST')
        env_db=getenv('HBNB_MYSQL_DB')
        self._engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                     .format(env_user, env_passwd,
                                             env_host, env_db),
                                     pool_pre_ping=True))
        if 'test' == getenv('HBNB_ENV'):
            Base.metadata.drop_all(tables)

    def all(self, cls=None):
        ''' Otro Comentario Cool '''
        sess = sessionmaker()
        sess.configure(bind=engine)
        self.__session = sess()
        class_ls = []
        if cls:
            try:
                class_ls = self.__session.query(eval(cls)).all()
            except:
                class_ls = self.__session.query(cls).all()
        else:
            class_ls += self.__session.query(User).all()
            class_ls += self.__session.query(State).all()
            class_ls += self.__session.query(City).all()
            class_ls += self.__session.query(Amenity).all()
            class_ls += self.__session.query(Place).all()
            class_ls += self.__session.query(Review).all()
        for element in class_ls:
            form = '{}.{}'.format(type(class_ls).__name__, class_ls.id)
        print(form)
