# Decorator = A function that extends the behavior of another function
#             w/o modifying the base function
#             Pass the base function as an argument to the decorator

#             @add_sprinkles
#             get_ice_cream("vanilla")

def add_sprinkles(func):
    def wrapper(*arg, **kwargs): # If you don't have this wrapper, the decorator will run as soon as it get @ mentioned
        print("*You add sprinkles 🎊*")
        func(*arg, **kwargs) # Without the "func", the original function under the @ will not be executed
    return wrapper

def add_fudge(func):
    def wrapper(*arg, **kwargs):
        print("*You add fudge 🍫*")
        func(*arg, **kwargs)
    return wrapper

@add_sprinkles # This function will get called if the wrapper is not included in the decorator function
@add_fudge
def get_ice_cream(flavor):
    print(f"Here is your {flavor} ice cream 🍨")

get_ice_cream("vanilla")