class Car:
    def __init__(self, brand, model, year, mileage):
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__mileage = mileage
        self.__is_on = False
        self.__fuel_tank = 50

    def get_brand(self):
        return self.__brand

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def get_mileage(self):
        return self.__mileage

    def set_brand(self, brand):
        self.__brand = brand

    def set_model(self, model):
        self.__model = model

    def set_year(self, year):
        self.__year = year

    def set_mileage(self, mileage):
        self.__mileage = mileage

    def start(self):
        if self.__check_fuel() > 5:
            self.__is_on = True
        else:
            print("Not enough fuel...")

    def stop(self):
        self.__is_on = False

    def __check_fuel(self):
        return self.__fuel_tank


car = Car("audi","A3",2013,40000)
car.start()