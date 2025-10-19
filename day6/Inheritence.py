class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Some sound")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks!")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} meows!")

d = Dog("Bruno")
c = Cat("Kitty")

for animal in (d, c):
    animal.speak()