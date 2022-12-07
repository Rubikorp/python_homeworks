my_file = 'my-file.txt'

with open(my_file, 'w', encoding='utf-8') as data:
    close_symbol = False
    while not close_symbol:
        word = input("Введите строку для записи: ")
        if word == '':
            close_symbol = True
        data.writelines(f'{word} \n')
