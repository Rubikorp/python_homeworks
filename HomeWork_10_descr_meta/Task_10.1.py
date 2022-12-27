'''
Создать не менее двух дескрипторов для атрибутов классов,
которые вы создали ранее в ДЗ
'''
import copy


class ValidationNoNegative:

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Не может быть отрицательным")
        instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class Road:
    length = ValidationNoNegative()
    width = ValidationNoNegative()

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def print_weight_road(self):
        weight = int((self.length * self.width * 25 * 5) / 1000)
        print(f'{weight} т')


obj = Road(20, 5000)
obj.print_weight_road()

# ------------------------------------------


class ValidationMatrixLength:

    def __set__(self, instance, value):
        if len(value) < 3:
            raise ValueError("Матрица не соответствует стандарту")
        instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class Matrix:
    matrix = ValidationMatrixLength()

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        s = ''
        for i in range(len(self.matrix)):
            s = s + '\t'.join(map(str, self.matrix[i])) + '\n'
        return s

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix):
            return None
        res = copy.deepcopy(self.matrix)
        for i in range(len(self.matrix)):
            for k in range(len(self.matrix[i])):
                res[i][k] = self.matrix[i][k] + other.matrix[i][k]
        return Matrix(res)


l1 = [[1, 2, 4],
      [3, 4, 5],
      [5, 6, 6]]
l2 = [[11, 21, 41],
      [31, 41, 51],
      [51, 61, 61]]
m = Matrix(l1)
s = Matrix(l2)
print(m)
z = m + s
print('z ')
print(z)
print(type(z))
