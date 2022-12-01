'''
Задача 2
Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
'''


def print_user(*args):
    for i in args:
        print(i, end=' ')


first_name = input('Введите имя: ')
last_name = input('Введите фамилию: ')
birth = input('введите дату рождения формата XX.XX.XXXX: ')
city = input('Введите город: ')
email = input('Введите email: ')
phone_number = input('Введите номер тлф:')

print_user(
    first_name,
    last_name,
    birth,
    city,
    email,
    phone_number
)
