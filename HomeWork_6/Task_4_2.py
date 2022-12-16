from random import randint

from memory_profiler import profile


@profile
def create_sort_arr():
    """Выделяет память, доп память не выделяется"""
    my_list = [randint(1, 100) for x in range(1, 10)]
    min_el = my_list[0]
    my_list2 = []
    for el in my_list:
        if el > min_el:
            my_list2.append(el)
        min_el = el

    return my_list2


create_sort_arr()

'''
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     6     22.3 MiB     22.3 MiB           1   @profile
     7                                         def create_sort_arr():
     8                                             """Выделяет память, доп память не выделяется"""
     9     22.3 MiB      0.0 MiB          12       my_list = [randint(1, 100) for x in range(1, 10)]
    10     22.3 MiB      0.0 MiB           1       min_el = my_list[0]
    11     22.3 MiB      0.0 MiB           1       my_list2 = []
    12     22.3 MiB      0.0 MiB          10       for el in my_list:
    13     22.3 MiB      0.0 MiB           9           if el > min_el:
    14     22.3 MiB      0.0 MiB           4               my_list2.append(el)
    15     22.3 MiB      0.0 MiB           9           min_el = el
    16                                         
    17     22.3 MiB      0.0 MiB           1       return my_list2
'''


@profile
def create_sort_arr():
    """Выделяет память, доп память не выделяется"""
    my_list = [randint(1, 100) for x in range(1, 10)]
    min_el = my_list[0]
    my_list2 = []
    for el in my_list:
        if el > min_el:
            my_list2.append(el)
        min_el = el

    min_el = None
    del my_list

    return my_list2


'''
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    40     22.3 MiB     22.3 MiB           1   @profile
    41                                         def create_sort_arr():
    42                                             """Выделяет память, доп память не выделяется"""
    43     22.3 MiB      0.0 MiB          12       my_list = [randint(1, 100) for x in range(1, 10)]
    44     22.3 MiB      0.0 MiB           1       min_el = my_list[0]
    45     22.3 MiB      0.0 MiB           1       my_list2 = []
    46     22.3 MiB      0.0 MiB          10       for el in my_list:
    47     22.3 MiB      0.0 MiB           9           if el > min_el:
    48     22.3 MiB      0.0 MiB           4               my_list2.append(el)
    49     22.3 MiB      0.0 MiB           9           min_el = el
    50                                         
    51     22.3 MiB      0.0 MiB           1       min_el = None
    52     22.3 MiB      0.0 MiB           1       del my_list
    53                                         
    54     22.3 MiB      0.0 MiB           1       return my_list2
'''

create_sort_arr()
