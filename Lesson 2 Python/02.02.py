elements = input("Введите несколько значений через пробел:").split()
max_idx = len(elements) - 1
for idx in range (0, max_idx, 2):
    idxx = idx + 1
    elements[idx], elements[idxx] = elements[idxx], elements[idx]
print(elements)

