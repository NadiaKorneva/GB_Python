# Задание 1
# strings = []
#
# while True:
#    with open('01.txt', 'a+') as f:
#        string = input("Введите строку: ")
#
#        if not string:
#            break
#
#        f.write(f"{string}\n")

# Задание 2

# with open('02.txt') as f:
#    rows = f.readlines()
#    expanded_rows = [row.split() for row in rows]
#
# rows_count, words_count = len(rows), sum([len(word_list) for word_list in expanded_rows])
#
# print(f"Всего строк - {rows_count}, всего слов - {words_count}")

# Задание 3
#
#with open('03.txt', 'r') as my_file:
#    salary = []
#    poor = []
#    my_list = my_file.read().split('\n')
#    for i in my_list:
#        i = i.split()
#        if int(i[1]) < 20_000:
#           poor.append(i[0])
#        salary.append(i[1])
#print(f'Оклад меньше 20.000 {poor}, средний оклад {sum(map(int, salary)) / len(salary)}')

# Задание 4

translations = {
    "One": "Один",
    "Two": "Два",
    "Three": "Три",
    "Four": "Четыре"
}

converted_rows = []

with open("04.txt") as input_data:
    for row in input_data:
        name, value = row.split(' - ')
        converted_rows.append(f"{translations[name]} - {value}")

with open("04_ru.txt", "w") as output_data:
    output_data.writelines(converted_rows)


# Задание 5

#def summary():
#    try:
#        with open('file_5.txt', 'w+') as file_obj:
#            line = input('Введите цифры через пробел: \n')
#            file_obj.writelines(line)
#            my_numb = line.split()

#            print(sum(map(int, my_numb)))
#    except IOError:
#        print('Ошибка в файле')
#    except ValueError:
#        print('Неправильно набран номер. Ошибка ввода-вывода')
#summary()

# Задание 6

subjects = {}

with open('06.txt') as f:
    for row in f:
        subject_info = row.split()
        name = subject_info[0].rstrip(':')

        subjects[name] = subject_info[1:]

result = {}

for key, value in subjects.items():
    result[key] = sum(
        [
            int(hours[:hours.index('(')])
            for hours in value
            if hours != '-'
        ]
    )

print(result)

# Задание 7

