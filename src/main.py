numbers = list(range(19))

double = list(map(lambda x: x * 2, numbers))
print(double)


filtered = list(filter(lambda x: 0 < x < 7, numbers))
print(filtered)
