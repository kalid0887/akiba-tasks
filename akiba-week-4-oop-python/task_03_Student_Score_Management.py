class Student:
    school_name = "Akiba Academy"
    def __init__(self,name, score, department):
        self.name = name
        self.score = score
        self.deparment = department

    def display(self):
        print(f"name: {self.name}, score: {self.score}, depaartment: {self.deparment}")


s1 = Student("kalid", 3.4, "soft")
s2 = Student("sudeys", 3.5, "it")
s3 = Student("ahmed", 3.6, "biomed")
s1.display()
s2.display()
s3.display()

s1.score = 3.7

s1.display()

"""
A class attribute is a variable defined inside a class but outside its methods. 
It is shared by all objects (instances) of that class. 
An instance attribute is a variable that belongs to a specific object, 
usually defined inside the __init__() method using self. 
Each object can have its own instance attribute values. 
For example, university can be a class attribute,
while name and age can be instance attributes.
"""