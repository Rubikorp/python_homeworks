'''
Задача 2
Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию,
оформить в виде списка. Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
'''
from random import randint

from memory_profiler import profile


@profile
def create_sort_arr():
    """Выделяет доп память, не освобождается"""
    my_list = [randint(1, 100) for x in range(1, 10)]
    min_el = my_list[0]
    my_list2 = []
    for el in my_list:
        if el > min_el:
            my_list2.append(el)
        min_el = el

    return my_list2

'''
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    15     22.0 MiB     22.0 MiB           1   @profile
    16                                         def create_sort_arr():
    17                                             """Выделяет доп память, не освобождается"""
    18     22.0 MiB      0.0 MiB          12       my_list = [randint(1, 100) for x in range(1, 10)]
    19     22.0 MiB      0.0 MiB           1       min_el = my_list[0]
    20     22.0 MiB      0.0 MiB           1       my_list2 = []
    21     22.0 MiB      0.0 MiB          10       for el in my_list:
    22     22.0 MiB      0.0 MiB           9           if el > min_el:
    23     22.0 MiB      0.0 MiB           3               my_list2.append(el)
    24     22.0 MiB      0.0 MiB           9           min_el = el
    25                                         
    26     22.0 MiB      0.0 MiB           1       return my_list2
'''


@profile
def create_sort_arr():
    """Выделяет доп память, освобождается"""
    my_list = [randint(1, 100) for x in range(1, 10)]
    min_el = my_list[0]
    my_list2 = []
    for el in my_list:
        if el > min_el:
            my_list2.append(el)
        min_el = el

    del my_list
    min_el = None

    return my_list2

'''
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    46     22.1 MiB     22.1 MiB           1   @profile
    47                                         def create_sort_arr():
    48                                             """Выделяет доп память, освобождается"""
    49     22.2 MiB      0.0 MiB          12       my_list = [randint(1, 100) for x in range(1, 10)]
    50     22.2 MiB      0.0 MiB           1       min_el = my_list[0]
    51     22.2 MiB      0.0 MiB           1       my_list2 = []
    52     22.2 MiB      0.0 MiB          10       for el in my_list:
    53     22.2 MiB      0.0 MiB           9           if el > min_el:
    54     22.2 MiB      0.0 MiB           3               my_list2.append(el)
    55     22.2 MiB      0.0 MiB           9           min_el = el
    56                                         
    57     22.2 MiB      0.0 MiB           1       del my_list
    58     22.2 MiB      0.0 MiB           1       min_el = None
    59                                         
    60     22.2 MiB      0.0 MiB           1       return my_list2
'''

create_sort_arr()
