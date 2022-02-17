"""
1. Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку определенных данных из файлов
info_1.txt, info_2.txt, info_3.txt и формирующий новый «отчетный» файл в формате CSV. Для этого:
Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие и считывание данных.
В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь значения параметров «Изготовитель
системы», «Название ОС», «Код продукта», «Тип системы». Значения каждого параметра поместить в соответствующий список.
Должно получиться четыре списка — например, os_prod_list, os_name_list, os_code_list, os_type_list. В этой же функции
создать главный список для хранения данных отчета — например, main_data — и поместить в него названия столбцов отчета в
виде списка: «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». Значения для этих столбцов также
оформить в виде списка и поместить в файл main_data (также для каждого файла);
Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой функции реализовать получение данных
через вызов функции get_data(), а также сохранение подготовленных данных в соответствующий CSV-файл;
Проверить работу программы через вызов функции write_to_csv().
"""
from chardet import detect
from glob import glob
import re
import csv

PATH = r'../less_2/docs'

def get_data_from_txt(path):
    os_prod_list =[]
    os_name_list = []
    os_code_list = []
    os_type_list = []
    result = [os_prod_list, os_name_list, os_code_list, os_type_list]
    columns = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']
    main_data = [columns, ]
    file_list = glob(path + '\\' + '*.txt')
    for file in file_list:
        with open(file, 'rb') as f:
            content = f.read()
        encoding = detect(content)['encoding']
        with open(file, 'r', encoding=encoding) as f:
            content = f.read()
            for i, col in enumerate(columns):
                data = re.findall(f'{col}.*', content)[0].split(':')
                data = re.sub('\s+', ' ', data[1])
                result[i].append(data)
    main_data.extend([list(el) for el in zip(os_prod_list, os_name_list, os_code_list, os_type_list)])
    return main_data


def write_to_csv(path=PATH):
    data = get_data_from_txt(path)
    with open(f'../less_2/docs/new.csv', mode='w', encoding='utf8') as f:
        F_N_WRITER = csv.writer(f)
        F_N_WRITER.writerows(data)


write_to_csv()