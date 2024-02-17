#!/usr/bin/python3
from models import Base
""" Import Base from models module """
class Rectangle(Base):
    """" Define Rectangle class with Base class as parent"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(self.id)
    
    """ Getter methods and  setter methods for atrributes """
    def get_width(self):
        return self.__width 

    """ set width """
    def set_width(self, value):
        if type(width) != int:
            raise TypeError(" width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    """ get height """
    def get_height(self):
        return self.__height 

    """ set height """
    def set_height(self, value):
        if type(height) != int:
            raise TypeError(" height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    """ get x """
    def get_x(self):
        return self.__x 

    """ set x """
    def set_x(self, value):
        if type(x) != int:
            raise TypeError(" x must be an integer")
        if value <= 0:
            raise ValueError(" x must be > 0 ")
        self.__x = value

    """ get y """
    def get_y(self):
        return self.__y

    """ set y """
    def set_y(self, value):
        if type(y) != int:
            raise TypeError(" y must be an integer")
        if value <= 0:
            raise ValueError(" y must be > 0")
        self.__y = value

    def area(self):
        return self.__width * self.__height

    """ Display public method """
    def display(self):
        if self.width == 0 or self.height == 0:
            print("")
            return
        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print("", end = "") for x in range(self.x)]
            [print("#", end = "") for w in range(self.width)]
            print("")

    """__str__ method """
    @publicmethod
    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)

    """ Update function """
    def update(self, *args):
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                wlif a == 4:
                    self.y = arg
                a += 1

            elif kwargs and len(kwargs) != 0:
                for k, v in kwargs.items():
                    if k == "id":
                        if v is None:
                            self.__init__(self.width, self.height, self.x, self.y)
                        else:
                            self.id = v
                        elif k == "width":
                            self.width = v
                        elif k == "height":
                            self.height = v
                        elif k == "x":
                            self.x = v
                        elif k == "y":
                            self.y = v


    @classmethod
    def to_dictionary(self):
        """ Method that returns representation of Rectangle dictionary """
        return {
                "id" : self.id, "width": self.width, "height": self.height, "x" : self.x, "y" : self.y}
        
    
