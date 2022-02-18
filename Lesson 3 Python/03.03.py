a = int(input("Введите первое число:"))
b = int(input("Введите второе число:"))
c = int(input("Введите третье число:"))

def my_func(a, b, c):
    items = [a, b, c]
    items.remove(min(items))

    return sum(items)


print(my_func(a, b, c))