# Nested loops = A loop within another loop (outer, inner)
#                outer loop:
#                    inner loop:

for x in range(3):
    for y in range(3):
        print(f"({x}, {y})")

for x in range(3):
    for y in range(5):
        print(y, end="")
    print()

print()
print("I am Steve")

rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
symbols = input("Enter the symbols: ")
for x in range(rows):
    for y in range(columns):
        print(symbols, end="")
    print()
