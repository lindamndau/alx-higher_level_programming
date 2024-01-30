#!/usr/bin/python3
class Rectangle:
    """Define Class"""
    def __init__(self, width=0, height=0):
        """ Initialize class """
        self.__width = width
        self.__height = height

        def width(self):
            """ Getter method """
            return self.__width

        def width(self, value):
            """ Setter method """
            if not isinstance(self.__width, int):
                raise TypeError("width must be an integer")
            if self.value < 0:
                raise ValueError("width must be >= 0")
            self.__width = width

        def height(self):
            """ Get Height method """ 
            return self.__height
    
        def height(self, value):
            """ Set height metthod """
            if not isinstance(self.__height, int):
                raise TypeError("height must be an integer")
            if self.value < 0:
                raise ValueError("width must be >= 0")
            self.__height = height
