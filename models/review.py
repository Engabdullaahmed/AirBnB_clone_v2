#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


class Review(BaseModel):
    """
    Definition of the Review class for the reviews table in the database.

    Attributes:
        __tablename__ (str): this attribute represents the table name,
        "reviews".
        text (str): this attribute represents a column containing a string
        (1024 characters) and the attribute can't be null.
        place_id (str): this attribute represents a column containing a
        string (60 characters) and this attribute can't be null.
        It is a foreign key to places.id.
        user_id (str): this attribute represents a column containing a string
        (60 characters) and it can't be null. Its a foreign key to users.id.

    Args:
        BaseModel (class): The BaseModel class.
        Base (class): The declarative Base class from SQLAlchemy.
    """

    __tablename__ = 'reviews'

    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
