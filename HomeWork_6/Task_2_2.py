__autor__ = 'Ruslan Bikmetov'

"""
Задача 2
Для списка реализовать обмен значений соседних элементов, 
т.е. значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. 
При нечетном количестве элементов последний сохранить на своем месте. 
Для заполнения списка элементов необходимо использовать функцию input().
"""

# index = 0
# element = input(f"Введите элемент {index}:")
# array = []
# while element != "end":  # Закрыть ввод
#     array.append(element)
#     index += 1
#     element = input(f"Введите элемент {index}:")
#
# print(array)
#
#
# def sort_array(arr):
#     length = len(arr)
#     ind = 0
#     if length % 2 != 0:
#         length -= 1
#     while length > ind:
#         x = arr[ind]
#         arr[ind] = arr[ind + 1]
#         arr[ind + 1] = x
#         ind += 2
#
#
# sort_array(array)
# print(array)

arr = [1, 2, 3, 4, 5, 6]


def sort_array(array):
    try:
        for ind, value in enumerate(array, 0):
            x = ind + 1
            if x % 2 == 0:
                continue
            else:
                array[ind] = array[ind + 1]
                array[ind + 1] = value
        return array
    except IndexError:
        return array


print(sort_array(arr))
