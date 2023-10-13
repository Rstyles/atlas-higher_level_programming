#!/usr/bin/python3
"""This Module contians the class Square
   Size and position are used to print a square using the '#' character
"""


class Square:
    """Defines a Square with a size and postion"""

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self) -> int:
        return self.__size

    @size.setter
    def size(self, value: int):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self) -> tuple[int, int]:
        return self.__position

    @position.setter
    def position(self, position: tuple[int, int]):
        if not isinstance(position[0], int) or not isinstance(position[1], int) or position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self) -> int:
        return self.__size**2

    def my_print(self):
        if self.__size == 0:
            print("")
        for i in range(self.__size):
            for k in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            print("")
