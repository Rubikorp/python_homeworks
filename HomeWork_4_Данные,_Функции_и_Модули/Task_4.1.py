'''
Задача 1
Реализовать скрипт,
в котором должна быть предусмотрена
функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.
Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
'''

from sys import argv

script_name, amount_hours, rate_per_hour, premium = argv

print(int(amount_hours) * int(rate_per_hour) + int(premium))
