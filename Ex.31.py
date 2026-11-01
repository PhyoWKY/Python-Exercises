# object = A "bundle" of related attributes (variable) and methods (functions)
#          E.g. phone, cup, book
#          You need a "class" to create many objects

# class = (blueprint) used to design the structure and layout of an object

from car_class import Car

car1 = Car("Ford", 2024, "red", False)
car2 = Car("Mustang", 2025, "blue", True)
car3 = Car("Tesla", 2026, "green", False)

print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale)
car1.drive()
car1.stop()
car1.describe()

print()

print(car2.model)
print(car2.year)
print(car2.color)
print(car2.for_sale)
car2.drive()
car2.stop()
car2.describe()

print()

print(car3.model)
print(car3.year)
print(car3.color)
print(car3.for_sale)
car3.drive()
car3.stop()
car3.describe()