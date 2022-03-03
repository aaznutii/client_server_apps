
import os
import select
import socket
import sys
import logging
import time

import logs.config_server_log
import argparse

from logs.log_func_actions import log
from logs.errors import IncorrectDataRecivedError
from common.utils import get_message, send_message
from common.variables import ACTION, PRESENCE, ACCOUNT_NAME, USER, RESPONSE, ERROR, TIME, DEFAULT_PORT, MAX_CONNECTIONS,\
    MESSAGE, MESSAGE_TEXT, SENDER

sys.path.append(os.path.join(os.getcwd(), '../'))

# Инициализация логирования сервера.
SERVER_LOGGER = logging.getLogger('server')


@log
def action_with_client_msg(message, messages_list, client):
    """ Функция обработки сообщения клиента"""

    SERVER_LOGGER.info(f'Начало работы функции action_with_client_msg')
    if ACTION in message and message[ACTION] == PRESENCE and TIME in message and USER in message \
            and message[USER][ACCOUNT_NAME] == 'Guest':
        SERVER_LOGGER.debug(f'Проверка action_with_client_msg структуры сообщения прошла успешно.{message}')
        send_message(client, {RESPONSE: 200})
        return

    elif ACTION in message and message[ACTION] == MESSAGE and TIME in message and MESSAGE_TEXT in message:
        SERVER_LOGGER.debug(f'Проверка action_with_client_msg структуры сообщения прошла успешно.{message}')
        messages_list.append((message[ACCOUNT_NAME], message[MESSAGE_TEXT]))
        return

    else:
        SERVER_LOGGER.debug(f'Функцией action_with_client_msg получено некорректное сообщение.{message}')
        return {RESPONSE: 400, ERROR: 'PRESENCE IS INVALID'}


@log
def arg_parser():
    """Парсер аргументов коммандной строки"""
    SERVER_LOGGER.info(f'Проверка указанных параметров')
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', default=DEFAULT_PORT, type=int, nargs='?')
    parser.add_argument('-a', default='', nargs='?')
    namespace = parser.parse_args(sys.argv[1:])
    listen_address = namespace.a
    listen_port = namespace.p

    # проверка получения корретного номера порта для работы сервера.
    if not 1023 < listen_port < 65536:
        SERVER_LOGGER.critical(
            f'Попытка запуска сервера с указанием неподходящего порта '
            f'{listen_port}. Допустимы адреса с 1024 до 65535.')
        sys.exit(1)

    return listen_address, listen_port


@log
def main():
    listen_address, listen_port = arg_parser()
    SERVER_LOGGER.info(
        f'Запущен сервер, порт для подключений: {listen_port}, '
        f'адрес с которого принимаются подключения: {listen_address}. '
        f'Если адрес не указан, принимаются соединения с любых адресов.')


    transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    transport.bind((listen_address, listen_port))
    transport.settimeout(0.5)

    # Очереди сообщений
    clients = []
    messages = []

    transport.listen(MAX_CONNECTIONS)

    while True:
        # Учет таймаута в подключениях
        try:
            client, client_address = transport.accept()
        except OSError as err:
            SERVER_LOGGER.debug(err.errno)
        else:
            SERVER_LOGGER.info(f'Установлено соединение с клиентом {client_address}')
            clients.append(client)

        #    Списки на отправку и прием
        recv_data_lst = []
        send_data_lst = []
        err_lst = []

        # Проверяем на наличие ждущих клиентов
        try:
            if clients:
                recv_data_lst, send_data_lst, err_lst = select.select(clients, clients, [], 0)
        except OSError:
            pass

        if recv_data_lst:
            for client_with_message in recv_data_lst:
                try:
                    action_with_client_msg(get_message(client_with_message),
                                           messages, client_with_message)
                except:
                    SERVER_LOGGER.info(f'Клиент {client_with_message.getpeername()} '
                                f'отключился от сервера.')
                    clients.remove(client_with_message)

        # Если есть сообщения для отправки и ожидающие клиенты, отправляем им сообщение.
        if messages and send_data_lst:
            message = {
                ACTION: MESSAGE,
                SENDER: messages[0][0],
                TIME: time.time(),
                MESSAGE_TEXT: messages[0][1]
            }
            del messages[0]
            for waiting_client in send_data_lst:
                try:
                    send_message(waiting_client, message)
                except:
                    SERVER_LOGGER.info(f'Клиент {waiting_client.getpeername()} отключился от сервера.')
                    waiting_client.close()
                    clients.remove(waiting_client)


if __name__ == '__main__':
    main()