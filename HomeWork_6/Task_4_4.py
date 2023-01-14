'''
Задача 4
Представлен список чисел.
Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию.
Элементы вывести в порядке их следования в исходном списке.
Для выполнения задания обязательно использовать генератор.
Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]
'''
from random import randint

from memory_profiler import profile


@profile
def create_rnd_uniq_list():
    """Выделяет доп память, не освобождается"""
    my_list = [randint(1, 44) for el in range(1, 16)]
    unique_numbers = [el for el in my_list if my_list.count(el) == 1]
    return unique_numbers


'''
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    16     22.2 MiB     22.2 MiB           1   @profile
    17                                         def create_rnd_uniq_list():
    18                                             """Выделяет доп память, не освобождается"""
    19     22.2 MiB      0.0 MiB          18       my_list = [randint(1, 44) for el in range(1, 16)]
    20     22.2 MiB      0.0 MiB          18       unique_numbers = [el for el in my_list if my_list.count(el) == 1]
    21     22.2 MiB      0.0 MiB           1       return unique_numbers
'''

create_rnd_uniq_list()


@profile
def create_rnd_uniq_list():
    """Выделяет доп память, освобождается"""
    my_list = [randint(1, 44) for el in range(1, 16)]
    unique_numbers = [el for el in my_list if my_list.count(el) == 1]

    del my_list

    return unique_numbers


'''
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    26     22.2 MiB     22.2 MiB           1   @profile
    27                                         def create_rnd_uniq_list():
    28                                             """Выделяет доп память, освобождается"""
    29     22.2 MiB      0.0 MiB          18       my_list = [randint(1, 44) for el in range(1, 16)]
    30     22.2 MiB      0.0 MiB          18       unique_numbers = [el for el in my_list if my_list.count(el) == 1]
    31                                         
    32     22.2 MiB      0.0 MiB           1       del my_list
    33                                         
    34     22.2 MiB      0.0 MiB           1       return unique_numbers
'''

create_rnd_uniq_list()
