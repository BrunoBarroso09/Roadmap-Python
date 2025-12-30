# Object orientation programming

class MyClass:
    name = "Peter"
    age = 22

    def my_information(self):
        print(f"My name is {self.name} and I have {self.age} years.")

myinfo = MyClass()
print(myinfo.name, myinfo.age)
myinfo.my_information()