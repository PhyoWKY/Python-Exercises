# List comprehension = A concise way to create lists in Python
#                      Compact and easier to read than traditional loops
#                      [expression for value in iterable if condition

doubles = []
for x in range(1, 11):
    doubles.append(x * 2)
print(doubles) # This is the traditional way

print()

doubles = [x * 2 for x in range(1, 11)] # List comprehension
triples = [y * 3 for y in range(1, 11)]
squares = [z * z for z in range(1, 11)]
print(doubles)
print(triples)
print(squares)

print()

fruits = ["apple", "banana", "cherry"]
fruits = [fruit.upper() for fruit in fruits]
print(fruits)

fruit_chars = [fruit[0] for fruit in fruits]
print(fruit_chars)

print()

numbers = [1, -2, 3, -4, 5, -6, 8, -7]
positive_num = [num for num in numbers if num >= 0]
print(positive_num)

negative_num = [num for num in numbers if num < 0]
print(negative_num)

even_num = [num for num in numbers if num % 2 == 0]
print(even_num)

odd_num = [num for num in numbers if num % 2 != 0]
print(odd_num)

print()

grades = [85, 42, 79, 90, 56, 61, 30]
passing_grades = [grade for grade in grades if grade >= 60]
print(passing_grades)

