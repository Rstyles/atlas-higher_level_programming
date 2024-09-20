#!/usr/bin/python3
""" Random documentation """
from models.tmp_rectangle import Rectangle


class Rectangle(Rectangle):
    """ Random documentation """

    @classmethod
    def save_to_file(cls, list_objs):
        """ Random documentation """
        if list_objs is None or len(list_objs) > 0:
            super().save_to_file(list_objs)
