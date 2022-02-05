"""
4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления в байтовое
и выполнить обратное преобразование (используя методы encode и decode).
"""

WORDS_LIST = ['разработка', 'администрирование', 'protocol', 'standard']


def get_bytes_from_words(words_list):
    result_list = []
    for el in words_list:
        el = el.encode()
        print(f'Преобразование: {el}: Тип - {type(el)}: Длинна - {len(el)}')
        if len(el) != len(el.decode()):
            print('Невозможно записать в байтовом типе.\n')
        result_list.append(el)
    return result_list


def get_words_from_bytes(bytes_list):
    print('\n============Преобразование в слова из байтов============')
    for el in bytes_list:
        el = el.decode()
        print(f'Преобразование: {el}: Тип - {type(el)}: Длинна - {len(el)}')


get_words_from_bytes(get_bytes_from_words(WORDS_LIST))