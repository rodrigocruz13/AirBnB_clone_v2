#!/usr/bin/python3
"""This is the amenity class"""

from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """This is the class for Amenity
    Attributes:
        name: input name
    """

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=True, primary_key=True)
        place_amenities = relationship("Place", secondary="place_amenity")

    else:
        name = ""
