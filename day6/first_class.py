# first_class.py
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says Woof!")

my_dog1 = Dog("Buddy", "Golden Retriever")
my_dog2 = Dog("Bruno", "Labrador")
my_dog1.bark()
my_dog2.bark()