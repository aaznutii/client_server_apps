"""
6. Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет», «декоратор».
 Далее забыть о том, что мы сами только что создали этот файл и исходить из того, что перед нами файл в неизвестной
 кодировке. Задача: открыть этот файл БЕЗ ОШИБОК вне зависимости от того, в какой кодировке он был создан.
"""

from chardet import detect


def create_file_txt():
    list_to_file = ['сетевое программирование', 'сокет', 'декоратор']
    with open('../less_1/docs/test_file.txt', 'w', encoding='utf8') as f:
        f.writelines('\n'.join(list_to_file))


create_file_txt()


def get_undef_file():
    with open('../less_1/docs/test_file.txt', 'rb') as f:
        content = f.read()
    encoding = detect(content)['encoding']
    print('encoding: ', encoding)

    # --- 3. Теперь открываем файл в УЖЕ известной нам кодировке
    with open('../less_1/docs/test_file.txt', encoding=encoding) as f_n:
        for el_str in f_n:
            print(el_str, end='')
        print()


get_undef_file()
