"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""
import subprocess
import chardet

ARGS = [['ping', 'yandex.ru'], ['ping', 'youtube.com']]

for args in ARGS:
    PING = subprocess.Popen(args, stdout=subprocess.PIPE)
    for line in PING.stdout:
        result = chardet.detect(line)
        line = line.decode(result['encoding']).encode('utf-8')
        print(line.decode('utf-8'))

# YA_PING = subprocess.Popen(ARGS, stdout=subprocess.PIPE)
# for line in YA_PING.stdout:
#     result = chardet.detect(line)
#     line = line.decode(result['encoding']).encode('utf-8')
#     print(line.decode('utf-8'))
#

