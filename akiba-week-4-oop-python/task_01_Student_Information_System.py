class Student:
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department

    def display_info(self):
        print(f"name: {self.name}, age: {self.age}, department: {self.department}")


s1 = Student("kalid", 22, "soft")
s2 = Student("sudeys", 22, "it")
s3 = Student("ahmed", 22, "biomed")
s1.display_info()
s2.display_info()
s3.display_info()
