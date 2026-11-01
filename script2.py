
from script1 import *

# print(__name__)

def favorite_drink(drink):
    print(f"Your favorite drink is {drink}")

def main():
    print("This is script2")
    favorite_food("apple")    # This imports from script1 but don't run all the script1 file
    favorite_drink("soda")
    print("Goodbye")

if __name__ == "__main__":    # This means run the main code only if it runs directly from the original script 
    main()