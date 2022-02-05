"""
5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового в строковый тип
на кириллице.
"""

import chardet   # необходима предварительная инсталляция!
import subprocess
import platform

COUNT = 2
PING_TO_LIST = ['yandex.ru', 'youtube.com']


def get_pings(count, ping_to_list):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    for el in ping_to_list:
        args = ['ping', param, str(count), el]
        result = subprocess.Popen(args, stdout=subprocess.PIPE)
        for line in result.stdout:
            result = chardet.detect(line)
            line = line.decode(result['encoding']).encode('utf-8')
            print(line.decode('utf-8'))


get_pings(COUNT, PING_TO_LIST)
