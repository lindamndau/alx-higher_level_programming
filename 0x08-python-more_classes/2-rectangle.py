#!/usr/bin/python3
class Rectangle:
    """Define class"""
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        def width(self):
            """ Get and retrieve method """
            return self.__width

        def width(self, value):
            if not isinstance(self, int):
                raise TypeError("width must be an integer")
            if self.value < 0:
                raise ValueError("width must be >= 0")
            self.__width = width

        def height(self):
            return self.__height

        def height(self, value):
            if not isinstance(self, int):
                raise TypeError("height must be an integer")
            if self.value < 0:
                raise ValueError("height must be an integer")
            self.__height = height

    def area(self):
        total_area = self.__width * self.__height
        return total_area
        
    def perimeter(self):
        if self.__width or self.__height == 0:
            perimeter = 0
        else:
            per = 2 * (self.__width + self.__height)
            return per
self = Rectangle()
self.area()
self.perimeter()
