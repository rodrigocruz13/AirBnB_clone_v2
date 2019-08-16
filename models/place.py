#!/usr/bin/python3
"""This is the place class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, Float, String, ForeignKey
from os import getenv
from sqlalchemy import Table
from sqlalchemy.orm import relationship
from models.review import Review

"""
Add an instance of SQLAlchemy Table called place_amenity for creating
the relationship Many-To-Many between Place and Amenity:
table name place_amenity
metadata = Base.metadata
2 columns:
place_id, a string of 60 characters foreign key of places.id, primary
key in the table and never null
amenity_id, a string of 60 characters foreign key of amenities.id,
primary key in the table and never null
"""
if getenv('HBNB_TYPE_STORAGE') == 'db':
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places.id'),
                                 primary_key=True, nullable=False),
                          Column('amenity_id',
                                 String(60),
                                 ForeignKey('amenities.id'),
                                 primary_key=True, nullable=False))

"""
Update Place class:
for DBStorage: class attribute amenities must represent a relationship with
    the class Amenity but also as secondary to place_amenity with option
    viewonly=False (place_amenity has been define previously)
for FileStorage:
Getter attribute amenities that returns the list of Amenity instances
based on the attribute amenity_ids that contains all Amenity.id linked
to the Place
Setter attribute amenities that handles append method for adding an
Amenity.id to the attribute amenity_ids. This method should accept only
Amenity object, otherwise, do nothing.

"""


class Place(BaseModel, Base):
    """This is the class for Place
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night:: pice for a staying in int
        latitude: latitude in flaot
        longitude: longitude in float
        amenity_ids: list of Amenity ids
    """

    __tablename__ = 'places'
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship('Review', backref='place', cascade='delete')
        amenities = relationship(
            'Amenity', secondary=place_amenity, viewonly=False)

    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            review_ls = []
            objects = storage.all(Review)
            for k, v in objects.items():
                if v.place_id == self.id:
                    review_ls.append(v)
            return review_ls

        """
        Getter attribute amenities that returns the list of Amenity instances
        based on the attribute amenity_ids that contains all Amenity.id linked
        to the Place
        """
        @property
        def amenities(self):
            amenities_ls = []
            objects = storage.all(Amenity)
            for k, v in objects.items():
                if v.amenity_id == self.id:
                    amenities_ls.append(v)
            return amenities_ls

        """
        Setter attribute amenities that handles append method for adding an
        Amenity.id to the attribute amenity_ids. This method should accept
        only Amenity object, otherwise, do nothing.
        """
        @amenities.setter
        def amenities(self, obj):
            if isinstance(obj, Amenity):
                amenity_ids.append(obj.id)
