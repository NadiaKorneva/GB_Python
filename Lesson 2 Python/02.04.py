string = input("Введите строку из нескольких слов >>> ").split()
for idx, value in enumerate(string, start=1):
    print(f"{idx}. {value[:10]}")