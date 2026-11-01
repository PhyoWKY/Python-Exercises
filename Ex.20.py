# Function = a block of reusable code
#            place () after the function name to invoke it
#            This one is positional argument

def happy_birthday():
    print("Happy Birthday to you!")
    print("You survive another year!")
    print("Happy Birthday to you!")

happy_birthday()

print()

def happy_birthday(name, age):
    print(f"Happy Birthday to {name}!")
    print(f"You are {age} years old!")
    print("You survive another year!")
    print(f"Happy Birthday to {name}!")

happy_birthday("Me", 30)

print()

def display_invoice(username, amount, due_date):
    print(f"Hello {username}.")
    print(f"Your bill of ${amount:.2f} is due in {due_date}.")

display_invoice("Me", 50.25, "2020")

print()


# return = statement used to end a function
#          and send a result back to the caller

def add(x, y):
     z = x + y
     return z

def subtract(x, y):
    z = x - y
    return z

def multiply(x, y):
    z = x * y
    return z

def divide(x, y):
    z = x / y
    return z

print(add(10, 20))
print(subtract(10, 20))
print(multiply(10, 20))
print(divide(10, 20))

print()

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("John", "Smith")
print(full_name)