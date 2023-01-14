"""
Задача 5.4
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу,
открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""


my_file = "Task_5.4.txt"

translater = {
    'One': 'один',
    'Two': 'два',
    'Three': 'три',
    'Four': 'четыре'
}
with open(my_file, "r+", encoding="utf-8") as file_obj:
    my_list = []
    result = []
    try:
        for line in file_obj:
            tokens = line.split(" - ")
            print(tokens)
            if tokens[0] in translater:
                word = translater[tokens[0]]
                result.append(word + ' - ' + tokens[1])
        print(result)
    except IOError:
        print("Произошла ошибка ввода-вывода!")

    try:
        file_obj.writelines(result)
    except IOError:
        print("Произошла ошибка ввода-вывода!")


