class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def get_length(self):
        return self.__length

    def get_width(self):
        return self.__width

    def set_length(self, length):
        self.__length = length

    def set_width(self, width):
        self.__width = width


rectangle = Rectangle(10, 5)
print(rectangle.get_width())
rectangle.set_width(50)
print(rectangle.get_width())
