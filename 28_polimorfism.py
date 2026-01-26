class Animal():
    def emit_sound(self):
        return NotImplementedError("Method not implemented")

class Cat(Animal):
    def emit_sound(self):
        return "Meow!"

class Dog(Animal):
    def emit_sound(self):
        return "Bark!"

cat = Cat()
print(cat.emit_sound())

dog = Dog()
print(dog.emit_sound())