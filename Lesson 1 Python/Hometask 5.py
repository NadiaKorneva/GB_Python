revenue = int(input("Выручка:"))
costs = int(input("Издержки:"))

fin_result = revenue - costs

if fin_result > 0:
    print(f'Прибыль = {fin_result}')
    return_on_revenue = revenue / costs
    print(f'Рентабельность выручки = {return_on_revenue}')

    emploees = int(input("Количество сотрудников:"))
    profit_per_emploee = fin_result / emploees
    print(f'Прибыль на 1 сотрудника = {profit_per_emploee}')

else:
    print(f'Убыток = {fin_result}')


