# Collection = single "variable" used to store multiple values
#   List     = [] ordered and changeable. Duplicates OK
#   Set      = {} unordered and immutable, but Add/Remove OK. NO duplicates
#   Tuples   = () ordered and unchangeable. Duplicates OK. FASTER

fruits = ["apple", "banana", "cherry", "pineapple", "orange"]

"""
print(fruits[2])
print(fruits[0:3])
print(fruits[:3])
print(fruits[::3])
print(fruits[::-1])

for fruit in fruits: 
    print(fruit)
"""

fruits[0] = "grape"
fruits.append("melon")
fruits.remove("pineapple")
fruits.insert(1, "orange")
fruits.sort()
fruits.reverse()
# fruits.clear()

print(fruits)
print("apple" in fruits)
print(len(fruits))
print(fruits.index("grape"))
print(fruits.count("orange"))

# print(dir(fruits))
# print(help(fruits))

fruits = {"apple", "banana", "cherry", "pineapple", "orange", "orange"}

fruits.add("banana")
fruits.remove("pineapple")
fruits.pop()
# fruits.clear()
print(fruits)

# print(fruits[1])

# print(dir(fruits))
# print(help(fruits))

fruits = ("apple", "banana", "cherry", "pineapple", "orange", "orange")

print(fruits.index("orange"))
print(fruits.count("orange"))
print(fruits)

for fruit in fruits:
    print(fruit)

# print(dir(fruits))
# print(help(fruits))
