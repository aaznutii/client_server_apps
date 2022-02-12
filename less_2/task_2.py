"""
2. Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с информацией о заказах.
Написать скрипт, автоматизирующий его заполнение данными. Для этого:
Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item), количество (quantity),
цена (price), покупатель (buyer), дата (date). Функция должна предусматривать запись данных в виде словаря в файл
orders.json. При записи данных указать величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра.
"""
import json


def write_order_to_json(*args):
    """
    :param args: item, quantity, price, buyer, date = args
    :return: dont return
    write_order_to_json file
    """
    item, quantity, price, buyer, date = args
    data = {"orders": [{'item': item}, {'quantity': quantity}, {'price': price}, {'buyer': buyer}, {'date': date}]}
    with open('../less_2/docs/orders.json', mode='w', encoding='utf8') as f:
        json.dump(data,f, ensure_ascii=False,indent=4)


write_order_to_json('product', 5, 36000.36, 'Иванов Иван Иванович', "25.02.2022")
