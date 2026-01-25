class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def ShowInformation(self):
        return f"Name: {self.name} | surnane: {self.surname} | age: {self.age}"

class Man(Human):
    def __init__(self, name, surname, age):
        super().__init__(name, age)
        self.surname = surname

    def Sex(self):
        print("I'm a man")

p1 = Man("Peter", "Parker", 22)
print(p1.ShowInformation())
p1.Sex()