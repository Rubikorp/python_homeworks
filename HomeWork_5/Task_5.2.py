"""
Задача 5.2
Создать текстовый файл (не программно),
сохранить в нем несколько строк,
выполнить подсчет количества строк,
количества слов в каждой строке.
"""


my_file = 'Task_5.2.txt'

with open(my_file, 'r', encoding='utf-8') as data:
    stroces = [line for line in data]
    print(f'в документе {my_file}: {len(stroces)} строки')
    num_stroke = 0
    for stroce in stroces:
        num_stroke += 1
        print(f'В строке {num_stroke}: {len(stroce.split())} слова')
