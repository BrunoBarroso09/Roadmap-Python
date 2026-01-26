# Object orientation programming

class MyClass:
    name = ""
    age = 0

    def my_information(self):
        print(f"My name is {self.name} and I have {self.age} years.")

myinfo = MyClass()
myinfo.name = "Peter"
myinfo.age = 22
myinfo.my_information()