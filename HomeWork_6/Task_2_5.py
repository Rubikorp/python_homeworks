__autor__ = 'Ruslan Bikmetov'

"""
Задача 5
  Реализовать структуру «Рейтинг», 
  представляющую собой не возрастающий набор натуральных чисел. 
  У пользователя необходимо запрашивать новый элемент рейтинга. 
  Если в рейтинге существуют элементы с одинаковыми значениями, 
  то новый элемент с тем же значением должен разместиться после них.
"""


# number = int(input("Введите число: "))
#
# my_list = [7, 5, 3, 3, 2]
#
# while number != 0:  #конец программы
#     my_list.append(number)
#     my_list.sort()
#     my_list.reverse()
#     print(my_list)
#     number = int(input("Введите число: "))
# ----------------------------------------------------

def append_ratting():
    my_list = [7, 5, 3, 3, 2]
    number = 3
    my_list.append(number)
    my_list.sort(reverse=True)
    return my_list

print(append_ratting())