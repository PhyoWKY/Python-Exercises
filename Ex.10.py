# Indexing = accessing elements of a sequence using [] (indexing operator)
#            [start : end : step]

credit_number = "1234-5678-9012-3456"

"""print(credit_number[4])
print(credit_number[:7])
print(credit_number[3:])
print(credit_number[3:8])
print(credit_number[-4])
print(credit_number[::3])"""

last_digit = credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digit}")

print(credit_number[::-1])
print(credit_number[::-2])


# For more online help, visit doc.python.org or devdoc.io