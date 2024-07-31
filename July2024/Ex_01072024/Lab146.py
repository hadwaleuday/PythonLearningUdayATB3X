# Constructor
# Self, super, __init__
# public, _ , __ private

# Abstraction
# Abstraction - OOPs
# Hiding the details and showing the what is required

from abc import ABC, abstractmethod
class Animal(ABC):

    def __init__(self, name):
        self.name = name
    @abstractmethod
    def sound(self):
        pass


class Cat(Animal):

    def sound(self):
        print("meow meow")
    def walk(self):
        print("Cat walk")


class Dog(Animal):
    def sound(self):
        return "Bark"


cat = Cat("CAT")
cat.walk()
cat.sound()

dog = Dog("rancho")
print(dog.sound())