"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""

words = ['разработка', 'администратирование', 'protocol', 'standart']
ENBYTES_WORDS = []
for word in words:
    ENBYTES_WORDS.append(word.encode('utf-8'))
print(ENBYTES_WORDS)
DEBYTES_WORDS = []
for byte in ENBYTES_WORDS:
    DEBYTES_WORDS.append(byte.decode('utf-8'))
print(DEBYTES_WORDS)

