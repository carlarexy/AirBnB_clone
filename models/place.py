#!/usr/bin/python3
"""Defines Place class"""

from models.base_model import BaseModel


class Place(BaseModel):
    """"place class the handles the location of the apartments"""
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 2
    number_bathrooms = 2
    max_guest = 2
    price_by_night = 2
    latitude = 2.0
    longitude = 2.0
    amenity_ids = []
