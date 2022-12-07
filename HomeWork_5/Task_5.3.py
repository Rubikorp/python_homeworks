my_file = 'Task_5.3.txt'


def list_employees(data_file):
    lines = [line for line in data_file]
    employees = []
    for line_employee in lines:
        arr = line_employee.split()
        employee = {"name": arr[0], "cash": float(arr[1])}
        employees.append(employee)
        if employee["cash"] < 20000:
            print(f'{employee["name"]} {employee["cash"]}, получает меньше 20 000 руб')
    return employees


def average_income_f(employees):
    average_income = 0
    number_employees = 0
    for income in employees:
        number_employees += 1
        average_income += income["cash"]
    average_income = average_income / number_employees
    print(f'Средняя доходность сотрудников: {round(average_income, 2)}')


with open(my_file, 'r', encoding='utf-8') as data:
    average_income_f(list_employees(data))
