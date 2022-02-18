def delimiter(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return("Деление на 0!!")

a = int(input("Введите делимое:"))
b = int(input("Введите делитель:"))
result = delimiter(a, b)

print(result)