"""
Задание 2.

Каждое из слов «class», «function», «method» записать в байтовом формате
без преобразования в последовательность кодов
не используя!!! методы encode и decode)
и определить тип, содержимое и длину соответствующих переменных.

Подсказки:
--- b'class' - используйте маркировку b''
--- используйте списки и циклы, не дублируйте функции
"""

words = [b'class', b'function', b'method']

# def convert_byte(string_arr):
#     collect = {}
#     for i in string_arr:
#         byte_arr = []
#         i_bytes = bytes(i, 'utf-8')
#         for byte in i_bytes:
#             byte_arr.append(byte)
#         bytes_str = ''
#         for k in byte_arr:
#             bytes_str = bytes_str + f' {k}'
#         collect[i] = bytes_str
#
#     for key, value in collect.items():
#         print(f"{key}: {value}")
#
#
# convert_byte(words)

array = {}
for w in words:
    byte_arr = []
    for byte in w:
        byte_arr.append(byte)
    bytes_str = ''
    for k in byte_arr:
        bytes_str = bytes_str + f' {k}'
    array[w] = [type(w), len(w), bytes_str]
for key, value in array.items():
    print(f'{key}: {value}')