__autor__ = 'Ruslan Bikmetov'

"""
Задача 2
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""

second = int(input("Введите секунды:"))
minuts = second // 60
second = second % 60
hours = minuts // 60
minuts = minuts % 60
print(f'{hours}:{minuts}:{second}')

