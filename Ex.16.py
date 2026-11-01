fruits = ["apple", "banana", "cherry"]
vegetables = ["celery", "carrots", "turkey"]
meats = ["chicken", "fish", "turkey"]

groceries = [fruits, vegetables, meats]

print(groceries)
print(groceries[0])
print(groceries[0][1])
print()

for collection in groceries:
    for fruit in collection:
        print(fruit, end=" ")
    print()