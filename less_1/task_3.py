

"""
3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе. Важно: решение
 должно быть универсальным, т.е. не зависеть от того, какие конкретно слова мы исследуем.
"""
# Если я верно понял задачу, конечно

WORDS_LIST = ['attribute', 'класс', 'функция', 'type']


def get_bytes_from_words(words_list):
    for el in words_list:
        print(f'Содержание - {el}: Тип - {type(el)}: Длинна - {len(el)}')
        print(f'Содержание - {bytes(el, encoding="utf-8")}: '
              f'Тип - {type(bytes(el, encoding="utf-8"))}: '
              f'Длинна - {len(bytes(el, encoding="utf-8"))}')
        if len(el) != len(bytes(el, encoding="utf-8")):
            print('Невозможно записать в байтовом типе.\n')


get_bytes_from_words(WORDS_LIST)