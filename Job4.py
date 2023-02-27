class Character:
    def __init__(self, name, firstname):
        self.name = name
        self.firstname = firstname

    def introduce_myself(self):
        print("My name is", self.name, self.firstname)


person_1 = Character("Milo", "Joe")
person_2 = Character("Dupond", "Jean")

person_1.introduce_myself()
person_2.introduce_myself()
