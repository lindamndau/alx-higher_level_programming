#!/usr/bin/python3
class Rectangle:
    """Define Class"""
    def __init__(self, width=0, height=0):
        """ Initialize class """
        self.width = width
        self.height = height
        
        @property
        def width(self):
            """ Getter method """
            return self.__width
        
        @width.setter
        def width(self, value):
            """ Setter method """
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value

        @property
        def height(self):
            """ Get Height method """ 
            return self.__height

        @height.setter
        def height(self, value):
            """ Set height metthod """
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__height = value
