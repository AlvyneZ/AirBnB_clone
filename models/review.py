#!/usr/bin/python3
"""
This "review.py" module defines one class:
    Review(BaseModel) - defines attributes of a review
"""
from .base_model import BaseModel


class Review(BaseModel):
    """
    Class that defines a Review class to manage review details

    Attrs:
        place_id (string): Place being reviewed
        user_id (string): User reviewing the place
        text (string): The text of the review itself
    """
    place_id = ""
    user_id = ""
    text = ""
