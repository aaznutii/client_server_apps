"""
4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления в байтовое
и выполнить обратное преобразование (используя методы encode и decode).
"""

WORDS_LIST = ['разработка', 'администрирование', 'protocol', 'standard']


def get_bytes_from_words(words_list):
    for el in words_list:
        el = el.encode()
        print(f'Преобразование: {el.encode()}: Тип - {type(el)}: Длинна - {len(el)}')
        print(f'Содержание - {bytes(el, encoding="utf-8")}: '
              f'Тип - {type(bytes(el, encoding="utf-8"))}: '
              f'Длинна - {len(bytes(el, encoding="utf-8"))}')
        if len(el) != len(bytes(el, encoding="utf-8")):
            print('Невозможно записать в байтовом типе.\n')


get_bytes_from_words(WORDS_LIST)