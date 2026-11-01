# Static methods = A method that belong to a class rather than any object from that class (instance)
#                  Usually used for general utility functions

# Instance methods = Best for operations on instances of the class (objects)
# Static methods = Best for utility functions that do not need to class data

# Reminder, instance methods are the functions inside an individual class
# self.name is the instance variable

class Employee:
    def __init__(self, name, position): # This is the constructor used for initializing the instance variables
        self.name = name # These self.name are the actual instance variables
        self.position = position

    def get_info(self): # This method(function) is the instance method, instance means belong to the class it is in
        return f'{self.name} = {self.position}'

    @staticmethod
    def is_valid_position(position):
        valid_position = ["Manager", "Cashier", "Cook", "Janitor"]
        return position in valid_position

# staticmethod doesn't rely on the object, therefore no need to create the object to use that function
# No need to write "employee_1 = Employee.is_valid_position"

print(Employee.is_valid_position("Manager"))
print(Employee.is_valid_position("Driver"))

print()

employee1 = Employee("John", "Manager")
employee2 = Employee("Bob", "Cashier")
employee3 = Employee("Caine", "Cook")

# For the instance method, you will need to create the object(employee1) to have access to the class

print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())