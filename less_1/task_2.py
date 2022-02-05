

"""
2. Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность кодов
(не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.
"""
# Если я верно понял задачу, конечно

WORDS_LIST = ['class', 'function', 'method']


def get_bytes_from_words(words_list):
    for el in words_list:
        print(f'Содержание - {el}: Тип - {type(el)}: Длинна - {len(el)}')
        print(f'Содержание - {bytes(el, encoding="utf-8")}: '
              f'Тип - {type(bytes(el, encoding="utf-8"))}: '
              f'Длинна - {len(bytes(el, encoding="utf-8"))}')


get_bytes_from_words(WORDS_LIST)
