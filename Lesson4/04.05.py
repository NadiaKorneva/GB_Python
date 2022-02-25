from functools import reduce

numbs = [x for x in range(100, 1001) if x % 2 == 0]
print(numbs)

multiply = reduce(lambda x, y: x * y, numbs)

print(multiply)