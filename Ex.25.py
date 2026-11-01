# Membership operators = used to test a value or variable is found in a sequence
#                        (string, list, tuple, set, or dictionary)
#                        1. in
#                        2. not in

word = "APPLE"

letter = input("Guess a letter in the word: ")

if letter in word:
    print(f"There is {letter} in the word")
else:
    print(f"{letter} is not in the word")

if letter not in word:
    print(f"{letter} is not in the word")
else:
    print(f"There is {letter} in the word")

print()

students = {"Tom", "Jerry", "Kit"}

student = input("Enter the name of the student: ")

if student in students:
    print(f"{student} is a student")
else:
    print(f"{student} is not a student")

if student not in students:
    print(f"{student} was not found")
else:
    print(f"{student} is a student")

print()

grades = {"Timmy": "A",
          "George": "B",
          "Bob": "C",
          "Rebeca": "D"}
student = input("Enter the name of a student: ")

if student in grades:
    print(f"{student}'s grade is {grades[student]}")
else:
    print(f"{student} was not found")

print()

email = "TrueMan57@gmail.com"

if "@" in email and "." in email:
    print(f"{email} is a valid email")
else:
    print(f"{email} is not a valid email")