km = int(input("Введите километры в 1й день:"))
km_goal = int(input("Введите цель в км:"))

day = 1

while km < km_goal:
    day += 1
    km += km * .10
else:
    print(f"Вы достигните цель на день {day}")
