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


def append_ratting():
    my_list = [7, 5, 3, 3, 2]
    number = 3
    my_list.append(number)
    my_list.sort(reverse=True)
    return my_list


def find_season(month):
    season = [
        {"зима": [12, 1, 2]},
        {"весна": [3, 4, 5]},
        {"лето": [6, 7, 8]},
        {"осень": [9, 10, 11]}
    ]

    for i in season:
        for x in i.values():
            if month in x:
                time = str(i.keys())
                return time


def print_type_list(arr):
    type_arr = []
    for i in arr:
        type_arr.append(type(i))
    return type_arr


def full_time(second):
    minuts = second // 60
    second = second % 60
    hours = minuts // 60
    minuts = minuts % 60
    time = f'{hours}:{minuts}:{second}'
    return time


def sum_count(n):
    summa = n + n * 11 + n * 111
    return summa


def day_result(first_km, res_km):
    day = 1
    while first_km < res_km:
        first_km += first_km / 10
        day += 1
    return f'{day} день результата'


def find_max_number_in_count(number):
    count = 0
    maximum = 0
    while number > 0:
        count = number % 10
        number = number // 10
        if count > maximum:
            maximum = count
    return maximum


def deduplication(a, b):
    try:
        return round(a / b, 1)
    except ZeroDivisionError:
        return 'На ноль делить нельзя!!!'


def tittle_word(words: str):
    return words.title()