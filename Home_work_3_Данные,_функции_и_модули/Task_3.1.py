'''
Задача 1
Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление.
Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль.
'''


def deduplication(a, b):
    try:
        print(round(a / b, 1))
    except ZeroDivisionError:
        print('На ноль делить нельзя!!!')


n = int(input('введите делимое: '))
x = int(input('введите делитель: '))

deduplication(n, x)
