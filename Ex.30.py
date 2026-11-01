# if __name__ == __main__ : (This script can be imported OR run standalone)
#                           Function and classes in this module can be reused
#                           without the main block of code executing

# Good practice (code is modular,
#                helps readability,
#                leaves no global variables,
#                avoid unintended execution)

# e.g. library = import library for functionality
#               when running library directly, display a help page

def main():
    print("Hi")   #  Your program goes here

if __name__ == '__main__':
    main()

