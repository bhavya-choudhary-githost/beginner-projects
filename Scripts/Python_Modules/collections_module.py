from collections import Counter, namedtuple, defaultdict, deque

# Counter
a = 'aaaaaaannnnnnnndddddieeee'
b = {'a':'b', 'c':'d'}
counter_1 = Counter(a)
counter_2 = Counter(b)
print(counter_1)
print(list(counter_1.elements()))
print (counter_2.items(), counter_2.keys())
print()
print(counter_1.most_common(3)[0][0])

# namedtuple
Point = namedtuple('Point', ['x', 'y'])
point = Point(10, 20)
print(point)
print(point.x, point.y)

# defaultdict
default_dict = defaultdict(int)
default_dict['a'] = 1
default_dict['b'] = 'hello'
default_dict['c'] += 1  # Default value for 'c' is 0
print(default_dict)    

# deque
deque_example = deque([1, 2, 3, 4, 5])
deque_example.append(6)
deque_example.appendleft(0)
print(deque_example)
deque_example.pop()
deque_example.popleft()
print(deque_example)

# deque with maxlen
deque_maxlen = deque(maxlen=3)
deque_maxlen.append(1)
deque_maxlen.append(2)
deque_maxlen.append(3)
deque_maxlen.append(4)
print(deque_maxlen)
deque_maxlen.appendleft(0)
print(deque_maxlen)
deque_maxlen.pop()
print(deque_maxlen)
