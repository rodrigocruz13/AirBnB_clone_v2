#!/usr/bin/python3
"""
This is the Database storage class for AirBnB:
"""

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

"""
# class_dc = {'BaseModel': BaseModel, 'User': User,
# 'State': State, 'City': City, 'Amenity': Amenity,
# 'Place': Place, 'Review': Review}
"""


class DBStorage:
    """
    This class serializes instances to a JSON file and
    deserializes JSON file to instances
    Args:
        HBNB_XXX: Env sys variables.
    Attributes:
        __engine: DB engine instance
        __session: objects will be stored
    """

    __engine = None
    __session = None

    def __init__(self):
        """
        Gets the sys env variables & creates an apropriated engine
        """

        env_1 = getenv('HBNB_ENV')
        user_1 = getenv('HBNB_MYSQL_USER')
        pwd_1 = getenv('HBNB_MYSQL_PWD')
        host_1 = getenv('HBNB_MYSQL_HOST')
        db_1 = getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user_1, pwd_1,
                                              host_1, db_1),
                                      pool_pre_ping=True)

        """ Maps and manages the session with all tables """
        self.reload()

        """ Drop all tables stored in this metadata """
        if 'test' == env_1:
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
            List certaint types of objects.
            If cls is None, list all objs. If not it'll list all cls-objs
        """

        class_ls = []
        key_val = {}

        if cls:
            class_ls = self.__session.query(cls).all()

        else:
            class_ls += self.__session.query(User).all()
            class_ls += self.__session.query(State).all()
            class_ls += self.__session.query(City).all()
            class_ls += self.__session.query(Amenity).all()
            class_ls += self.__session.query(Place).all()
            class_ls += self.__session.query(Review).all()

        for element in class_ls:
            form = '{}.{}'.format(type(element).__name__, element.id)
            key_val[form] = element

        return key_val

    def new(self, obj):
        """
        Place an object in the Session. Its state will be persisted
        to the database on the next flush operation.
        """

        self.__session.add(obj)

    def save(self):
        """
        Commit the current transaction. It always issues flush() beforehand
        to flush any remaining state to the database
        """

        self.__session.commit()

    def delete(self, obj=None):
        """
        Mark an instance as deleted.
        The database delete operation occurs upon flush().
        """

        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        1. Base.metadata.create_all. Maps the data sent by engine
        2. Session. Establishes all conversations with the DB & represents
           a holding zone for all the loaded objs during its lifespan
        2a. Scoped_session: Provides management of Session objects.
        """

        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(expire_on_commit=False,
                                                     bind=self.__engine))()

    def close(self):
        """
        Close this Session. This clears all items and ends any
        transaction in progress.
        """

        self.__session.close()
