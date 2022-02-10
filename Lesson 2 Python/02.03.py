#lists
months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
month = int(input("Введите номер месяца:"))
if month < 3:
    print("зима")
elif month < 6:
    print("весна")
elif month < 9:
    print("лето")
elif month < 12:
    print("осень")
else:
    print("зима")


#dicts
month = int(input("Введите номер месяца:"))
seasons = {
    "зима": (1, 2, 12),
    "весна": (3, 4, 5),
    "лето": (6, 7, 8),
    "осень": (9, 10, 11)
}
for key, value in seasons.items():
    if month in value:
        print(f"{key}")

