__autor__ = 'Ruslan Bikmetov'

"""
Задача 6
Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
Программа должна принимать значения параметров a и b и  выводить одно натуральное число — номер дня.
"""

a = float(input("Введите кол-во киллометров в первый день: "))
b = float(input("Введите желаемое кол-во киллометров: "))
day = 1
while a < b:
    a += a/10
    day += 1
print(f'{day} день результата')
