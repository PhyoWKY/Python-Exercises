# While Loop = execute some code WHILE some conditions remains true

num = float(input("Enter a number between 0 and 10  : "))
while not 0 < num < 10:
    print(f"{num} is not a valid number")
    num = float(input("Enter a number between 0 and 10  : "))

print(f"Your number is {num}")