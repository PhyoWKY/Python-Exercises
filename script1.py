
# from script2 import *     # * means everything

# print(dir()) # 'dir' meaning directory

# print(__name__) # __name__ is called dunder name, dunder meaning double underscore

def favorite_food(food):
    print(f"Your favorite food is {food}")

def main():
    print("This is script1")
    favorite_food("pizza")
    print("Goodbye")

if __name__ == '__main__':
    main()                 # This will make the code run only in script1 even if run from script2

"""def favorite_food(food):
    print(f"Your favorite food is {food}")

print("This is script1")  # This will make the code run in script2 which we don't want it
favorite_food("pizza")
print("Goodbye")"""