#!/usr/bin/python3
class Rectangle:
    """Define class"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

        @property
        def width(self):
            """ Get and retrieve method """
            return self.__width
        
        @width.setter
        def width(self, value):
            """ setter method """
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value

        @property
        def height(self):
            """ Height Getter """
            return self.__height
        
        @height.setter
        def height(self, value):
            """ setter method """
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be an integer")
            self.__height = value

    def area(self):
        """ Total area of Rectangle """
        return self.__width * self.__height
        
    def perimeter(self):
        """ Total Rectangle perimeter """
        if self.__width or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)
Rectangle.area()
Rectangle.perimeter()
