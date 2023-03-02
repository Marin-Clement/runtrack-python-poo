class People:
    def __init__(self):
        self.age = 14

    def show_age(self):
        print(self.age)

    def say_hello(self):
        print("Hello")

    def modify_age(self, age):
        self.age = age


class Student(People):

    def go_to_school(self):
        print("Im going to school")

    def show_age(self):
        print(self.age)


class Teacher(People):
    def __init__(self, subject):
        super().__init__()
        self.subject = subject

    def teach(self):
        print("Im gonna start")


people = People()

student1 = Student()
student1.modify_age(15)
student1.say_hello()
student1.go_to_school()
student1.show_age()

teacher1 = Teacher("History")
teacher1.modify_age(40)
teacher1.say_hello()
teacher1.teach()
teacher1.show_age()
