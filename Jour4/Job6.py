class Vehicle:
    def __init__(self, brand, model, year, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price

    def vehicle_info(self):
        print(f"brand: {self.brand}\n"
              f"model: {self.model}\n"
              f"year: {self.year}\n"
              f"price: {self.price}\n")

    def start(self):
        print("Im rolling")


class Car(Vehicle):
    def __init__(self, brand, model, year, price):
        super().__init__(brand, model, year, price)
        self.doors = 4

    def vehicle_info(self):
        print(f"brand: {self.brand}\n"
              f"model: {self.model}\n"
              f"year: {self.year}\n"
              f"price: {self.price}\n"
              f"doors: {self.doors}\n")

    def start(self):
        print("Im rolling because im a car\n")


class Motorbike(Vehicle):
    def __init__(self, brand, model, year, price):
        super().__init__(brand, model, year, price)
        self.wheels = 2

    def vehicle_info(self):
        print(f"brand: {self.brand}\n"
              f"model: {self.model}\n"
              f"year: {self.year}\n"
              f"price: {self.price}\n"
              f"wheels: {self.wheels}\n")

    def start(self):
        print("Im rolling because im Jhonny\n")


car1 = Car("audi", "A4", 2019, 50000)
car1.vehicle_info()
car1.start()

motorbike1 = Motorbike("yamaha", "1200 Vmax", 1987, 4500)
motorbike1.vehicle_info()
motorbike1.start()