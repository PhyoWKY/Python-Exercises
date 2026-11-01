# Random Numbers

import random

low = 1
high = 100
options = ("rock", "paper", "scissors")
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]


number1 = random.randint(low, high)
number2 = random.random()
option = random.choice(options)
random.shuffle(cards)

print(cards)
print(number1)
print(number2)
print(option)
