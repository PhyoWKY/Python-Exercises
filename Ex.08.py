# Conditional Expression = A one-line shortcut for the if-else statement (ternary operator)
#                           Print or assign one of the values based on a condition
#                           X if condition else Y

num = 5
print("Positive" if num > 0 else "Negative")
print("Even" if num % 2 == 0 else "Odd")

A = 6
B = 7
max_num = "A" if A > B else "B"
print(max_num)
min_num = "A" if A < B else "B"
print(min_num)

age = 13
print("Adult" if age >= 18 else "Child")
