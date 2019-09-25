# dog.py
class Dog:
# Required properties are defined inside the __init__ constructor method
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

# Methods are defined as their own named functions inside the class
    def bark(self):
        print(f"{self.name} goes Woof!")

    def sit(self):
        print(f"{self.name} is sitting! Good dog!")

    def roll_over(self):
        print(f"{self.name} is rolling over! Good dog!")


Dog.greeting = "Woah"

# asfasf
