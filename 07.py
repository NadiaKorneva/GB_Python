import json

companies_data = []

with open('firms07.txt') as input_data:
    companies_dict = {}
    profit_list = []

    for company_row in input_data:
        name, form, revenue, costs = company_row.split()

        profit = float(revenue) - float(costs)
        companies_dict[name] = profit

        if profit:
            profit_list.append(profit)

    companies_data.append(companies_dict)
    companies_data.append({
        "average_profit": round(sum(profit_list) / len(profit_list), 2)
    })

with open('firms07.json', 'w') as output_data:
    json.dump(companies_data, output_data)