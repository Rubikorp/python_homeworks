'''
Задача 3
 Реализовать функцию my_func(),
 которая принимает три позиционных аргумента,
 и возвращает сумму наибольших двух аргументов.
'''


def my_func(x, y, z):
    my_list = [x, y, z]
    my_list.sort()
    print(my_list[1] + my_list[2])


a = 1
b = 3
c = 4

my_func(a, c, b)
