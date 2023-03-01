class City:
    def __init__(self, name, number):
        self.__city_name = name
        self.__population = number
        print(f"Population of {self.__city_name} is: {self.__population}")

    def add_new_people(self):
        self.__population += 1

    def print_update_population(self):
        print(f"Updated population of {self.__city_name} is: {self.__population}")


class People:
    def __init__(self, name, age, city):
        self.__name = name
        self.__age = age
        self.__city = city
        self.add_to_population()

    def add_to_population(self):
        self.__city.add_new_people()


city1 = City("Paris", 1000000)
city2 = City("Marseille", 861635)

Human1 = People("Jhon", 45, city1)
Human2 = People("Myrtille", 4, city1)
Human3 = People("Chloé", 45, city2)

city1.print_update_population()
city2.print_update_population()
