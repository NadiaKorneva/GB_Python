numbs = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [numb for idx, numb in enumerate(numbs) if idx > 0 and numbs[idx - 1] < numb]
print(result)