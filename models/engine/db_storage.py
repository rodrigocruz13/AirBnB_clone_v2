#!/usr/bin/python3
"""This is the Database storage class for AirBnB"""
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import (create_engine)

#class_dc = {'BaseModel': BaseModel, 'User': User,
            #'State': State, 'City': City, 'Amenity': Amenity,
            #'Place': Place, 'Review': Review}

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
        env_1 = getenv('HBNB_ENV')
        user_1 = getenv('HBNB_MYSQL_USER')
        pwd_1 = getenv('HBNB_MYSQL_PWD')
        host_1 = getenv('HBNB_MYSQL_HOST')
        db_1 = getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                     .format(user_1, pwd_1,
                                             host_1, db_1),
                                     pool_pre_ping=True)
        self.reload()
        if 'test' == env_1:
            Base.metadata.drop_all(tables)

    def all(self, cls=None):
        ''' Otro Comentario Cool '''
        class_ls = []
        key_val = {}
        if cls:
            class_ls = self.__session.query(cls).all()
        else:
            #class_ls += self.__session.query(User).all()
            class_ls += self.__session.query(State).all()
            class_ls += self.__session.query(City).all()
            #class_ls += self.__session.query(Amenity).all()
            #class_ls += self.__session.query(Place).all()
            #class_ls += self.__session.query(Review).all()
        for element in class_ls:
            form = '{}.{}'.format(type(element).__name__, element.id)
            key_val[form] = element
        return key_val

    def new(self, obj):
        ''' Comentario cool '''
        self.__session.add(obj)

    def save(self):
        ''' Comentario del save'''
        self.__session.commit()

    def delete(self, obj=None):
        ''' Comentario del delete '''
        if obj:
            self.__session.delete(obj)

    def reload(self):
        ''' Comentario del inicio y reinicio de la sesion '''
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(expire_on_commit=False,
                                                     bind=self.__engine))()

    def close(self):
        ''' Comentario de cierre '''
        self.__session.close()
