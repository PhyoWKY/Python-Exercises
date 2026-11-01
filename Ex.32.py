# class variable = Shared among all instances of a class
#                  Defined outside the construction
#                  (While instance variables are inside the constructor of the class)
#                  Allow you to share data among all objects created from that class

class Student:

    class_year = 2019
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1

student1 = Student("Kit", 23)
student2 = Student("Valentina", 25)
student3 = Student("Tom", 35)
student4 = Student("James", 35)

print(Student.num_students)

print()

print(student1.name)
print(student1.age)
print(Student.class_year)

print()

print(student2.name)
print(student2.age)
print(Student.class_year)

print()

print(f"My graduation class of {Student.class_year} has {Student.num_students} students")
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)