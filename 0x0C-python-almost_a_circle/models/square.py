#!/usr/bin/python3

class Square(Rectangle):
    """ Define subclass Square of base class Reactangle """
    def __init__(self, size, x=0, y=0, id=None):

        super().__init__(size, size, x, y, id):
            """ super() call Sqaure inherits attributes from parent class Rectangle """
       @property 
        """ Getter method for width """
        def size(self):
            return self.width

        @size.setter
        """ Setter method for size """
        def size(self, value):
            self.width = value
            self.height = value
        
        @classmethod
        """ classmethod update """
        def update(self, *args, **kwargs):
            if args and len(args) != 0:
                a = 0
                for arg in args:
                    if a == 0:
                        if arg is None:
                            self.__init__(self.size, self.x, self.y)
                        else:
                            self.id = arg
                        elif a == 1:
                            self.size = arg
                        elif a == 2:
                            self.x = arg
                        elif a == 3:
                            self.y = arg
                        a += 1
                elif kwargs and len(kwargs) != 0:
                    for key, value in kwargs.items():
                        if k == "id":
                            if v is None:
                                self.__init__(self.size, self.x, self.y)
                            else:
                                self.id = v
                        elif k == "size":
                            self.size = v
                        elif k == "x":
                            self.x = v
                        elif k == "y":
                            self.y = v
            """ if args list is empty, create kwargs else skip"""
                """ Declare dictionery """

        def to_dictionary(self):
            return {"id": self.id, "x": self.x, "size": self.size, "y": self.y}

        def __str__(self):
            return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
