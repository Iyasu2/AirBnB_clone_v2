#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import getenv


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True, nullable=False),
                      )


class Place(BaseModel, Base):
    """ A place to stay """
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

    reviews = relationship('Review', cascade='all, delete', backref='place')
    amenities = relationship(
            'Amenity', secondary=place_amenity, viewonly=False)

    @property
    def reviews(self):
        """ FileStorage relationship between Place and Review """
        from models import storage
        from models.review import Review

        review_list = []
        for review in self.review_ids:
            review_list.append(Review.get(review))
        return review_list

    @property
    def amenities(self):
        """
        Returns the list of `Amenity` instances
        """
        from models import storage
        from models.amenity import Amenity

        amenity_list = []
        for amenity in self.amenity_ids:
            amenity_list.append(Amenity.get(amenity))
        return amenity_list

    @amenities.setter
    def amenities(self, obj=None):
        """
        handles append method for adding
    """
        if type(obj) is Amenity:
            self.amenity_ids.append(obj.id)
