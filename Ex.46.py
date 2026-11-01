# Python reading files (.txt, .json, .csv)

file_path = "D:/Courses & Lessons/PycharmProjects/Test/output.txt"

try:
    with open(file_path, "r") as file: # This 'file' here is the object
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found") # Using try and except method will prevent the program to throw in error
except PermissionError:
    print("You do not have permission to access that file")

print()

import json

file_path = "D:/Courses & Lessons/PycharmProjects/Test/job.json"

with open(file_path, "r") as file:
    content = json.load(file)
    print(content)
    print(content["name"])
    print(content["age"])
    print(content["job"])

print()

import csv

file_path = "D:/Courses & Lessons/PycharmProjects/Test/roles.csv"

with open(file_path, "r") as file:
    content = csv.reader(file)
    print(content) # This will give memory address

    print()

    for line in content:
      # print(line)
        print(line[0])

