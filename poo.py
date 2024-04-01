# POO

# Class
class Person:
    name: str
    age: int

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def say_hello(self) -> None:
        print(f"Hello, my name is {self.name} and I'm {self.age} years old.")


# Object
person = Person("John", 30)

person.say_hello()
