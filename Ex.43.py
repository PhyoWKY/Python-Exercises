# exception = An event that interrupts the flow of a program
#             (ZeroDivisionError, TypeError, ValueError)
#             1.try, 2.except, 3.finally

try:
    number = int(input("Enter a number: "))
    print( 1 / number )
except ZeroDivisionError:
    print("You can't divide by zero IDIOT!")
except ValueError:
    print("Enter only numbers please!")
except Exception: # (Bad approach)
    print("Something went wrong!")

# (The above 'Exception' is a bad approach as it look up everything)
# (We need to know, what went wrong)

finally:
    print("Do some cleanup stuff")

# for more info, go to docs.python.org