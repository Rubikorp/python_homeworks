'''
Задача 2
Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
'''


def print_user(
        first_name_user,
        last_name_user,
        birth_user,
        city_user,
        email_user,
        phone_number_user):
    print(f''
          f'{first_name_user} '
          f'{last_name_user}, '
          f'{birth_user}, '
          f'{city_user}, '
          f'{email_user}, '
          f'{phone_number_user}')


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
