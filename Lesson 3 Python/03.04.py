#1
x = float(input("Введите число:"))
y = int(input("Введите степень:"))

def my_func(x,y):
    return x ** y
print(my_func(x,y))


#2
x = float(input("Введите число:"))
y = int(input("Введите степень:"))

counter = x
if y > 0:
    for y in range(1, y):
        counter *= x
else:
    for y in range(1, y, -1):
        counter /= x
print(counter)


