class Animal:
    def __init__(self):
        self.age = 0
        print("J'ai:", self.age, "ans")
        self.name = None

    def ages(self):
        self.age += 1
        print("J'ai:", self.age, "ans")

    def names(self, name):
        self.name = name
        print("Mon nom:", self.name)


animal1 = Animal()
animal1.names("Milo")
animal1.ages()


