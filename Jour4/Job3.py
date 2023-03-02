class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def perimeter(self):
        return (self.__length + self.__width) * 2

    def surface(self):
        return self.__length * self.__width

    def get_length(self):
        return self.__length

    def get_width(self):
        return self.__width

    def set_length(self, length):
        self.__length = length

    def set_width(self, width):
        self.__width = width


class Parallelepiped(Rectangle):
    def __init__(self, height):
        super().__init__()
        self.height = height

    def volume(self):
        return self.get_width() * self.get_length() * self.height