# Class methods = Allow operations related to the class itself
#                 Take (cls) as the first parameter, which represents the class itself.

# Instance methods = Best for operations on instance of the class (objects)
# Static methods = Best for utility functions that do not need access to class data
# Class methods = Best for class-level data or require access to the class itself

class Student:

    count = 0 # This is class variable, it belongs to th entire class not just to the def method
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1 # This will increase for everytime __init__ runs
                           # e.g. if we create 2 objects, __init__ runs twice
        Student.total_gpa += gpa

    # This is the instance method
    def get_info(self):
        return f"{self.name} {self.gpa}"

    @classmethod
    def get_count(cls):
        return f"Total number of students: {cls.count}"

    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Average gpa: {cls.total_gpa/cls.count:.2f}"

student1 = Student("John", 3.2)
student2 = Student("Bob", 2.5)
student3 = Student("Timmy", 3.5)

print(Student.get_count())
print(Student.get_average_gpa())

