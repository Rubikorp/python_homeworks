my_file = "Task_5.5.txt"

with open(my_file, "w", encoding="utf-8") as data:
    data.write(input("Введите числа через пробел: "))

with open(my_file, "r", encoding="utf-8") as data:
    my_list = list(map(int, data.readline().split()))
    print(sum(my_list))
