import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def change_radius(self, radius):
        self.radius = radius

    def circonference(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * self.radius**2

    def diameter(self):
        return self.radius * 2

    def show_infos(self):
        print("R:", self.radius, "C:", round(self.circonference()), "A:", round(self.area()), "D:", self.diameter())


Circle(4).show_infos()
Circle(7).show_infos()
