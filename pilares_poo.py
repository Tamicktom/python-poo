

# extends example
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass
    
    def eat(self):
        print(f"{self.name} is eating.")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} says Woof!")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} says Meow!")

dog = Dog("Rex")
cat = Cat("Misty")

dog.speak()
dog.eat()
cat.speak()

# super() example