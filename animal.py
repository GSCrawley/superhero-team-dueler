class Animal:
    def __init__(self, name):
        self.name = name 

    def eat(self):
        print('{} is eating'.format(self.name))

    def drink(self):
        print('{} is drinking'.format(self.name))

class Frog(Animal):
    def jump(self):
        print('{} is jumping'.format(self.name))

frog = Frog("James")
frog.eat()
frog.drink()
frog.jump()