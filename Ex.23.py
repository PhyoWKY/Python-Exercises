# *args      = allows you to pass multiple non-key arguments
# **kwargs  = allows you to pass multiple keyword-arguments
#             * unpacking operator
#             1. positional, 2. default, 3. keyword, 4. ARBITRARY

def add(*args):
    total = 0
    for num in args:
        total += num
    return total

print(add(1, 2, 3, 4, 5, 6))

def add(*nums):
    total = 0
    for num in nums:
        total += num
    return total

print(add(1, 2, 3, 4, 5, 6))

print()

def display_name(*names):
    for name in names:
        print(name, end=" ")

display_name("Dr.", "Spongebob", "Harold", "Squarepants", "III")

print()
print()

def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_address(street="This St.",
              apt="100",
              city="Spring",
              state="CA",
              country="USA",
              zip="0101")

print()

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    if "apt" in kwargs:
        print(f"{kwargs.get('apt')} {kwargs.get('street')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('pobox')}")
        print(f"{kwargs.get('street')}")
    else:
        print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('state')} {kwargs.get('zip')}")
    print(f"{kwargs.get('country')}")


shipping_label("Dr.", "Spongebob", "Harold", "Squarepants", "III",
               street="This St.",
               #apt="No.100",
               pobox="PO Box No.100",
               city="Spring",
               state="CA",
               country="USA",
               zip="0101")