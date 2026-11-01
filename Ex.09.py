# Validate User Input

# 1. Username is no more than 12 characters
# 2. Username must not contain spaces
# 3. Username must not contain digits

username = input("Enter your name: ")

if len(username) > 12:
    print("Username can not be longer than 12 characters")
elif not username.find(" ") == -1:
    print("Username can not contain spaces")
elif not username.isalpha():
    print("Username can contain only alphanumeric characters")
else:
    print(f"Welcome {username}")
