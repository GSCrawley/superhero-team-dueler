# my-dogs.py
import dog

my_dog = dog.Dog("lil Bow-Wow", "Chihuahua")
print(f'{my_dog.name} is a {my_dog.breed}')

my_dog.bark()

my_second_dog = dog.Dog("Snoop Dogg", "Great Dane")
print(f'{my_second_dog.name} is a {my_second_dog.breed}')

my_second_dog.sit()

my_third_dog = dog.Dog("Ice Ice Doggy", "Mutt")
print(f'{my_third_dog.name} is a {my_third_dog.breed}')

my_third_dog.roll_over()


my_dog.bark()
my_second_dog.bark()
my_third_dog.bark()
