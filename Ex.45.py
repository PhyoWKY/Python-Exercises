# Python writing files (.txt, .json, .csv)

txt_data_1 = "I like bananas"

file_path = "output.txt"
           # This is Relative file path, it will create in the same folder as this current Python file

with open(file=file_path, mode="w") as file:
    file.write(txt_data_1)
    print(f"txt file '{file_path}' was created")

# "with" statement will automatically close the file after we're done reading it.
# It is typically a good practice to close a file to prevent unexpected behavior.
# 'w' for write, this is in the mode parameter
# 'x' for write when the file doesn't exist
# 'a' for append
# 'r' for read

print()

txt_data_2 = "I like bananas"

file_path = "D:/Courses & Lessons/PycharmProjects/Test/output.txt"
           # This is the Absolute file path, it will create in our desire folder

with open(file=file_path, mode="w") as file:
    file.write(txt_data_2)
    print(f"txt file '{file_path}' was created")

# This 'w' mode can also override the file

print()

txt_data_3 = "I like bananas"

file_path = "output.txt"

try:
    with open(file=file_path, mode="x") as file:
        file.write(txt_data_3)
        print(f"txt file '{file_path}' was created")
except FileExistsError:
    print("That file already exists")

# The 'x' mode can only write when there is no already existed file

print()

txt_data_4 = "I like Coding"

file_path = "D:/Courses & Lessons/PycharmProjects/Test/output.txt"

with open(file_path, "a") as file:
    file.write("\n" + txt_data_4)
    print(f"txt file '{file_path}' was created")

# This 'a' mode will add the text in the existing file

print()

employees = ["Eugene", "Squidward", "SpongeBob", "Patrick"]

file_path = "D:/Courses & Lessons/PycharmProjects/Test/employees.txt"

with open(file_path, "w") as file:
    for employee in employees:
        file.write(employee + "\n")
    print(f"txt file '{file_path}' was created")

print()

# .json file is made of key:value pair

import json

employee = {
    "name": "SpongeBob",
    "age": 30,
    "job": "cook"
}

file_path = "D:/Courses & Lessons/PycharmProjects/Test/job.json"

with open(file_path, "w") as file:
    json.dump(employee, file, indent=4) # 'dump' converts the dictionary to json string
    print(f"json file '{file_path}' was created")

print()

# .csv file means 'comma separated values', common in spreadsheet like Excel
# It uses the idea of 2d rows and columns

import csv

employees_2 = [["Name", "Age", "Job"],
               ["SpongeBob", 30, "Cook"],
               ["Patrick", 37, "Unemployed"],
               ["Sandy", 27, "Scientist"]]

file_path = "D:/Courses & Lessons/PycharmProjects/Test/roles.csv"

with open(file_path, "w", newline="") as file:
    writer = csv.writer(file) # This 'writer' is an object
    for row in employees_2:
        writer.writerow(row)
    print(f"csv file '{file_path}' was created")