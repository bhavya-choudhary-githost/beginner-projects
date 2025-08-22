import random
low = 5
high = 55
cards = ['K', 'Q', '2', '3', '4', '5', '6', '7', '8', '9', 'J', 'A']
options = ['rock', 'paper', 'scissors']

random_integer = random.randint(low, high)
random_float = random.random()
random.shuffle(cards)
option = random.choices(options)

for item in [random_integer, random_float, cards, option]:
    print(item)
    print()