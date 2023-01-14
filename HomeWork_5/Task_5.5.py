"""
Задача 5.5
Создать (программно) текстовый файл,
записать в него программно набор чисел,
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле
и выводить ее на экран.
"""


my_file = "Task_5.5.txt"

with open(my_file, "w", encoding="utf-8") as data:
    data.write(input("Введите числа через пробел: "))

with open(my_file, "r", encoding="utf-8") as data:
    my_list = list(map(int, data.readline().split()))
    print(sum(my_list))
