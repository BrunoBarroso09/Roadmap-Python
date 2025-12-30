# Object orientation programming

class Person:

    def __init__(self, my_name, my_age):
        self.name = my_name
        self.age = my_age

    def my_information(self):
        print(f"My name is {self.name} and I have {self.age} years.\n")

p1 = Person("Peter", 22)
p1.my_information()

p2 = Person("Anna", 27)
p2.my_information()