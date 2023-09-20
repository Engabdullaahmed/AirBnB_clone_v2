#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from models import storage
import os


class Place(BaseModel, Base):
    """
    The definition of the Place class for the places table in the database.
    """
    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    #     reviews = relationship('Review', back_populates='place',
    #                            cascade='all, delete-orphan')

    # # amenity_ids = []
    # else:

    #     @property
    #     def reviews(self):
    #         """This method gets the attribute to return the list of Review
    #         instances with place_id equals to the current place.id for
    #         DBStorage.
    #         """
    #         reviews_list = []
    #         reviews_dict = storage.all('Review')
    #         for review in reviews_dict.values():
    #             if review.place_id == self.id:
    #                 reviews_list.append(review)
    #         return reviews_list
