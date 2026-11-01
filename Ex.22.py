# keyword argument = an argument preceded by an identifier
#                    helps with readability
#                    order of arguments doesn't matter
#                    1. positional, 2. default, 3. KEYWORD, 4. arbitrary

def hello(greeting, title, first, last):
    print(f"{greeting} {title}{first} {last}")

hello(last = "Wick", title = "Mr.", first = "Luke", greeting = "Hello")
hello("Hello", last = "Wick", title = "Mr.", first = "Luke")

print()

for x in range(1, 11):
    print(x, end=" ")
#            This "end" here is keyword argument, default as end="\n"
print()
print("1", "2", "3", "4", "5", "6", "7", "8", "9", sep="-")

print()

def get_num(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_num(country=1, area=123, first=456, last=7890)
print(phone_num)