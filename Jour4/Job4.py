class Shape:
    def area(self):
        return 0


class Rectangle(Shape):
    def __init__(self, lenght, width):
        self.lenght = lenght
        self.width = width

    def area(self):
        return self.lenght * self.width


rectangle1 = Rectangle(10,20)
print(rectangle1.area())