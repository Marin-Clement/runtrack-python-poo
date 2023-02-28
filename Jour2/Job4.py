class Student():
    def __init__(self, name, first_name, student_number):
        self.__name = name
        self.__first_name = first_name
        self.__student_number = student_number
        self.__credits = 0
        self.__level = self.__student_eval()

    def add_credits(self, credits):
        if credits > 0:
            self.__credits += credits
            print(f"New solde: {self.__credits} !")
        else:
            print("Error")
        self.__level = self.__student_eval()

    def __student_eval(self):
        if self.__credits >= 90:
            return "Excellent"
        elif self.__credits >= 80:
            return "Very good"
        elif self.__credits >= 70:
            return "Good"
        elif self.__credits >= 60:
            return "Tolerable"
        elif self.__credits < 60:
            return "Insufficient"

    def student_info(self):
        print(f"name: {self.__name} | first name: {self.__first_name} | id: {self.__student_number} | Level: {self.__level}")


student = Student("Doe", "Jhon", 145)

for i in range(3):
    student.add_credits(30)
    student.student_info()
