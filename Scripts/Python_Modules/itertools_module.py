from itertools import (product, permutations, combinations, accumulate, groupby,
count, cycle, repeat)

#product
print(len(list(product('ABCD', repeat=2))))
a = [1, 2]
b = [3, 4]
print(list(product(a, b, repeat = 2))) #is equal to product(a, b, a, b)
print()

#permutations
print(list(permutations('ABCD', 2)))
print()

#combinations
print(list(combinations('ABCD', 2)))
print()

#accumulate
print(list(accumulate([1, 2, 3, 4, 5])))
print()

#groupby
a = [1, 2, 4, 57]

group = groupby(a, key = lambda x: x < 5)
for key, value in group:
    print(key, list(value))

b = [{'name': 'joseph', 'age': '57'}, {'name': 'jolyne', 'age': '17'},/
 {'name': 'jojo','age': '17'}]

#count
counter = count(start=5, step=2)
print(next(counter))  # 5
print(next(counter))  # 7       

#cycle
cycler = cycle('ABCD')
for _ in range(8):
    print(next(cycler), end=' ')  # A B C D A B C D

#repeat
repeater = repeat('Hello', times=3)
for item in repeater:
    print(item)  # Hello Hello Hello
print()

# Using repeat with no times argument
repeater_infinite = repeat('World')
for _ in range(3):
    print(next(repeater_infinite))  # World World World
print()