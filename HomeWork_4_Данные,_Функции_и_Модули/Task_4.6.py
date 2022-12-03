'''
Задача 6
Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.

Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным.
Необходимо предусмотреть условие его завершения.
'''

from itertools import cycle, count

count = int(input('введите целое число: '))
end_number = int(input('введите до какого числа создать список: '))

my_list = [el for el in range(count, end_number+1)]
print(my_list)

repeat = int(input('введите колличество повторений списка: '))

repeat_list = []
cycler = cycle(my_list)
while repeat_list.count(my_list[len(my_list) - 1]) != repeat:
    repeat_list.append(next(cycler))

print(repeat_list)
