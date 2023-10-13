#!/usr/bin/python3
"""This Module contians the class Square

Returns:
    _type_: Square
"""

class Square:
    """Defines a Square with a size and postion
    """

    def __init__(self, size=0, position=(0, 0)):
        """Create a Square to print in the console

        Args:
            size (int, optional): The size of the Square. Defaults to 0.
            position (tuple, optional): The position of the Square. Defaults to (0, 0).
        """
        self.__size = size
        self.__position = position

    @property
    def size(self) -> int:
        """Gets the size

        Returns:
            int: Returns the size
        """
        return self.__size

    @size.setter
    def size(self, value: int):
        """Sets the size property

        Args:
            value (int): The value of the size property

        Raises:
            TypeError: size must be an integer
            ValueError: size must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self) -> tuple[int, int]:
        """Gets the position

        Returns:
            tuple[int, int]: Returns the postion
        """
        return self.__position

    @position.setter
    def position(self, position: tuple[int, int]):
        """Sets the position property

        Args:
            position (tuple[int, int]): The position that will be set

        Raises:
            TypeError: position must be a tuple of 2 positive integers
        """
        if (
            not isinstance(position[0], int)
            or not isinstance(position[1], int)
            or position[0] < 0
            or position[1] < 0
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self) -> int:
        """Returns the area of the square

        Returns:
            int: Returns the area of the square
        """
        return self.__size**2

    def my_print(self):
        """Prints the square offset by the position
        """
        if self.__size == 0:
            print("")
        for i in range(self.__size):
            for k in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            print("")
