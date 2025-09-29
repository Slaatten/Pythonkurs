# Exercise 1: Range + slicing
numbers = list(range(20))
print(numbers[::3])  # every 3rd element


# Exercise 2: Unpacking
greater_numbers = [10, 20, 30, 40, 50]
first, second, *others = greater_numbers
print(first, second, others)


# Exercise 3: Enumerate
letters = ["a", "b", "c", "d"]
for index, letter in enumerate(letters):
    print(index, letter)


# Exercise 4: List methods
letters = ["a", "b", "c"]
letters.append("d")       # add at end
letters.insert(1, "x")    # insert at index 1
letters.remove("b")       # remove value
letters.pop(0)            # remove index 0
letters.clear()           # empty list


# Exercise 5: Membership + count
letters = ["a", "b", "c", "a"]
print("d" in letters)     # False
print(letters.count("a")) # 2


# Exercise 6: Sorting
numbers = [5, 2, 9, 1]
numbers.sort()
print(numbers)            # [1, 2, 5, 9]

new_numbers = sorted(numbers)
print(new_numbers)        # [1, 2, 5, 9]


# Exercise 7: Map (double numbers)
numbers = [1, 2, 3, 4]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)            # [2, 4, 6, 8]


# Exercise 8: Filter (even numbers)
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)              # [2, 4, 6]


# Exercise 9: Filter + Map combined
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
squares = list(map(lambda x: x * x, evens))
print(squares)            # [4, 16, 36]


# Exercise 10: Double numbers (list comprehension)
numbers = [1, 2, 3, 4]
doubled = [x * 2 for x in numbers]
print(doubled)            # [2, 4, 6, 8]


# Exercise 11: Filter even numbers (list comprehension)
numbers = [1, 2, 3, 4, 5, 6]
evens = [x for x in numbers if x % 2 == 0]
print(evens)              # [2, 4, 6]


# Exercise 12: Filter + square (list comprehension)
numbers = [1, 2, 3, 4, 5, 6]
squares = [x * x for x in numbers if x % 2 == 0]
print(squares)            # [4, 16, 36]

# Exercise 13: Zip & Falsy
Zip
names = ["Stian", "Ola", "Kari"]
ages = [22, 30, 25]

combined = list(zip(names, ages))
print(combined)

Falsy
x = ""
if not x:
    print("Falsy")

# Exercice 14: Stack LIFO
stack = []
stack.append(1)
stack.append(2)
stack.append(3)

stack.pop()
print(stack)
stack.pop()
print(stack)

if not stack:
    print("Empty stack")

# Exercise 15: Queues FIFO
from collections import deque
queue = deque([])

queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()
print(queue)

# Exercise 16: Tuples
point = (10, 20)
print(point[0])
point[0] = 50 # Gives Error

# Exercise 17: Sets
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)
print(a & b)
print(a - b)
print(a ^ b)

duplicates = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6, 6]
uniqes = list(set(duplicates))
print(uniqes)

# Exercise 18: Dictionaries
user = {"name": "Stian", "age": 25}
print(user)
user["city"] = "Oslo"
print(user)

print(user.get("password", "N/A"))

for key, value in user.items():
    print(key, value)

# Exercise 19: Comprehensions
numbers = list(range(10))
print(numbers)
sqaure = [x ** 2 for x in numbers]
print(sqaure)

streng = "Programming"
uniqes = {c for c in streng}
print(uniqes)

sqaures_dict = {x: x ** 2 for x in range(1, 6)}
print(sqaures_dict)

# Exercise 20: Unpacking
def add(a, b, c):
    return a + b + c


values = [1, 2, 3]

print(add(*values))

# Exercise Mosh
from pprint import pprint
sentence = "This is a common interview question"

char_frequency = {}

for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

char_frequency_sorted = sorted(char_frequency.items(),
                               key=lambda kv: kv[1],
                               reverse=True)
print(char_frequency_sorted[0])

