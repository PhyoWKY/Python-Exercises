# Iterables = An object/collection that can return its elements one at a time,
#             allowing it to be iterated over in a loop

numbers = [1, 2, 3, 4, 5]
for number in reversed(numbers):
    print(number, end=" ")

print()

numbers = (1, 2, 3, 4, 5)
for number in numbers:
    print(number, end=" ")

print()

fruits = {"apple", "banana", "cherry"}
for fruit in fruits:
    print(fruit)

name = "Bro Code"
for letter in name:
    print(letter, end=" ")

print()

my_dictionary  = {"A": 1, "B": 2, "C": 3, "D": 4}
for key in my_dictionary:
    print(key)
for value in my_dictionary.values():
    print(value)
for key, value in my_dictionary.items():
    print(f"{key} = {value}")