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
