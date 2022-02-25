#1
from itertools import count

for x in count(5, 1):
    if x > 15:
        break

    print(x)


#2
from itertools import cycle

numbs_list = [1, 2, 3, 4, 5]
с = 0
for el in cycle(numbs_list):
    if с > 10:
        break
    print(el)
    с += 1
