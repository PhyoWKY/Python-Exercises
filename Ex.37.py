# "Ducking typing" = Another way to achieve polymorphism besides Inheritance
#                    Object must have the minimum necessary attributes/methods
#                    "If it looks like a duck and quacks like a duck, it must be a duck."

class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEOW!")

class Car:

# Car isn't animal but if you somehow can make it speak or has "alive" attribute, it can be considered
# in animal class according to "Duck typing".

    alive = False
    def speak(self):
        print("HONK!")

animals = [Dog(), Cat(), Car()]
for animal in animals:
    animal.speak()
    print(animal.alive)