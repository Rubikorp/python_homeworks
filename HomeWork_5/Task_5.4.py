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


