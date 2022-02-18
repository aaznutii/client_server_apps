import json
import os
import socket
import sys
import logging
import logs.config_server_log
from logs.errors import IncorrectDataRecivedError
from common.utils import get_message, send_message
from common.variables import ACTION, PRESENCE, ACCOUNT_NAME, USER, RESPONSE, ERROR, TIME, DEFAULT_PORT, MAX_CONNECTIONS

sys.path.append(os.path.join(os.getcwd(), '../'))

# Инициализация логирования сервера.
SERVER_LOGGER = logging.getLogger('server')


def action_with_client_msg(message):
    SERVER_LOGGER.info(f'Начало работы функции action_with_client_msg')
    if ACTION in message and message[ACTION] == PRESENCE and TIME in message and USER in message \
            and message[USER][ACCOUNT_NAME] == 'Guest':

        SERVER_LOGGER.debug(f'Проверка action_with_client_msg структуры сообщения прошла успешно.{message}')
        return {RESPONSE: 200}
    else:
        SERVER_LOGGER.debug(f'Функцией action_with_client_msg получено некорректное сообщение.{message}')
        return {RESPONSE: 400, ERROR: 'PRESENCE IS INVALID'}


def main():
    SERVER_LOGGER.info(f'Начало работы функции main. Проверка указанных параметров')
    try:
        if '-p' in sys.argv:
            listen_port = int(sys.argv[sys.argv.index('-p') + 1])
            SERVER_LOGGER.info(f'Установлен порт: {listen_port}')
        else:
            listen_port = DEFAULT_PORT
            SERVER_LOGGER.info(f'Установлен порт по умолчанию: {DEFAULT_PORT}')
        if listen_port < 1024 or listen_port > 65535:
            raise ValueError
    except IndexError:
        SERVER_LOGGER.error(f'В функции main не указан номер порта после -p')
        # print('Необходимо указать номер порта после -p.')
        sys.exit(1)
    except ValueError:
        SERVER_LOGGER.error(f'В качестве порта может быть указано только число от 1024 до 65535')
        # print('В качестве порта может быть указано только число от 1024 до 65535')
        sys.exit(1)

    try:
        if '-a' in sys.argv:
            listen_address = sys.argv[sys.argv.index('-p') + 1]
            SERVER_LOGGER.info(f'Установлен адрес: {listen_address}')
        else:
            listen_address = ''
            SERVER_LOGGER.info(f'Адрес не установлен')
    except IndexError:
        SERVER_LOGGER.error(f'Необходимо указать адрес ip после -a.')
        # print('Необходимо указать адрес ip после -a.')
        sys.exit(1)
    except ValueError:
        SERVER_LOGGER.critical(f'Может быть указано только число от 1024 до 65535')
        # print('Может быть указано только число от 1024 до 65535')
        sys.exit(1)

    transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    transport.bind((listen_address, listen_port))

    transport.listen(MAX_CONNECTIONS)

    while True:
        client, client_address = transport.accept()
        SERVER_LOGGER.info(f'Установлено соединение с клиентом {client_address}')
        try:
            msg_from_client = get_message(client)
            SERVER_LOGGER.debug(f'Получено сообщение от клиента {msg_from_client}')
            response = action_with_client_msg(msg_from_client)
            SERVER_LOGGER.info(f'Cформирован ответ клиенту {response}')
            send_message(client, response)
            SERVER_LOGGER.debug(f'Соединение с клиентом {client_address} закрывается.')
            client.close()
        except json.JSONDecodeError:
            SERVER_LOGGER.error(f'Не удалось декодировать JSON строку, полученную от '
                                f'клиента {client_address}. Соединение закрывается.')
            client.close()
        except IncorrectDataRecivedError:
            SERVER_LOGGER.error(f'От клиента {client_address} приняты некорректные данные. '
                                f'Соединение закрывается.')
            client.close()


if __name__ == '__main__':
    main()
