from sys import argv

work_hours, hour_cost, bonus = argv

salary = (float(hour_cost) * float(work_hours)) + float(bonus)

print(f"Заработная плата = {salary}")

