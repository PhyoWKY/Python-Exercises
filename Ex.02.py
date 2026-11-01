# Shopping Cart Program

item = input("What would you like to buy?: ")
price = float(input("The price of the item is: "))
quantity = int(input("How many items would you like?: "))
total_price = price * quantity
print(f"You have bought {quantity} items of {item}.")
print(f"The total price is ${round(total_price, 2)}")

