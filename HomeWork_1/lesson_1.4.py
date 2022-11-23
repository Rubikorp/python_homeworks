__autor__ = 'Ruslan Bikmetov'

"""
Задача 4
Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""

number = int(input("Введите число: "))
count = 0
maximum = 0
while number > 0:
    count = number % 10
    number = number // 10
    if count > maximum:
        maximum = count
print(maximum)
