# default argument = A default value for certain parameters
#                    default is used when that argument is omitted
#                    make your functions more flexible, reduces # of arguments
#                    1. positional 2. DEFAULT, 3. keyword, 4. arbitrary

def net_price(list_price, discount = 0.0, tax = 0.05):
    return list_price * (1 - discount) * (1 + tax)

print(net_price(
    500, 0.2))

print()

import time

def count(end, start = 0):
    for x in range(start, end + 1):
        print(x)
        time.sleep(1)
    print("DONE!")
    return count

count(30, 15)