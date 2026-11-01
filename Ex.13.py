# For loops = execute a block of code a fixed number of time.
#             You can iterate over a range, string, sequence, etc.


for x in reversed(range(1, 11)):
    print(x)
print("Happy New Year")

for x in range(1, 11, 3):
    print(x)

credit_card = "1234-5678-9012"
for x in credit_card:
    print(x)

for x in range(1, 21):
    if x == 13:
        continue
    else:
        print(x)

for x in range(1, 21):
    if x == 13:
        break
    else:
        print(x)

for x in range(3):
    print("Attempt", x + 1, (x + 1) * ".")

for x in range(1, 11, 2):
    print("Attempt", x, x  * ".")

name = "I am Steve"
for x in name:
    print(x)
for x in range(len(name)):
    print(x)

count = 0
for x in range(1, 10):
    if x % 2 == 0:
        print(x)
        count += 1
print(f"We have {count} even numbers")
