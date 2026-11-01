# Python file detection

import os # To let python have access to os(operating system)

file_path1 = "text.txt" # This is Relative file path, exist in the same folder as current Python file

if os.path.exists(file_path1):
    print(f"The location '{file_path1}' exists")
else:
    print(f"The location '{file_path1}' does not exist")

print()

file_path2 = "stuff/text.txt"
if os.path.exists(file_path2):
    print(f"The location '{file_path2}' exists")
else:
    print(f"The location '{file_path2}' does not exist")

print()

file_path3 = "D:\\Courses & Lessons\\PycharmProjects\\Test"
if os.path.exists(file_path3):
    print(f"The location '{file_path3}' exists")

    if os.path.isfile(file_path3):
        print("That is a file")
    elif os.path.isdir(file_path3):
        print("That is a directory")

else:
    print(f"The location '{file_path3}' does not exist")

# When copying the Absolut file path(C:\Users\) make sure to use \\ or /