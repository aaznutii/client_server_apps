"""
3. Задание на закрепление знаний по модулю yaml. Написать скрипт, автоматизирующий сохранение данных в файле
YAML-формата. Для этого:
Подготовить данные для записи в виде словаря, в котором первому ключу соответствует список, второму — целое число,
третьему — вложенный словарь, где значение каждого ключа — это целое число с юникод-символом, отсутствующим в кодировке
ASCII (например, €);
Реализовать сохранение данных в файл формата YAML — например, в файл file.yaml. При этом обеспечить стилизацию файла с
помощью параметра default_flow_style, а также установить возможность работы с юникодом: allow_unicode = True;
Реализовать считывание данных из созданного файла и проверить, совпадают ли они с исходными.
"""

import yaml

DATA_TO_YAML = {'1': [el for el in 'Test text'], '2': 1523, '3': {'1_€': 1, '2_€': 'text', '3_€': None}}

with open('../less_2/docs/data_write_2.yaml', 'w', encoding='utf-8') as f_n:
    yaml.dump(DATA_TO_YAML, f_n, default_flow_style=False, allow_unicode = True)

with open('../less_2/docs/data_write_2.yaml', 'r', encoding='utf-8') as f_n:
    DATA_FROM_YAML = yaml.load(f_n, Loader=yaml.FullLoader)

print(DATA_TO_YAML == DATA_FROM_YAML)