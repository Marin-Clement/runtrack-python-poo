class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show_points(self):
        print("X:", self.x, "Y:", self.y)

    def show_x(self):
        print("X:", self.x)

    def show_y(self):
        print("Y:", self.y)

    def change_x(self, x):
        self.x = x

    def change_y(self, y):
        self.y = y


point1 = Point(1, 2)

point1.show_points()
point1.change_x(5)
point1.show_points()
