import json
import socket
import sys
import time
import logging
import logs.config_client_log
from logs.errors import ReqFieldMissingError
from common.utils import send_message, get_message
from common.variables import ACTION, PRESENCE, TIME, USER, ACCOUNT_NAME, RESPONSE, DEFAULT_IP_ADDRESS, DEFAULT_PORT

# Инициализация клиентского логера
CLIENT_LOGGER = logging.getLogger('client')


def create_presence(account_name='Guest'):
    result = {
        ACTION: PRESENCE,
        TIME: time.time(),
        USER: {ACCOUNT_NAME: account_name},
    }
    CLIENT_LOGGER.debug(f'Сформировано {PRESENCE} сообщение для пользователя {account_name}')
    return result


def action_with_server_msg(message):
    CLIENT_LOGGER.debug(f'Разбор сообщения от сервера: {message}')
    if RESPONSE in message:
        if message[RESPONSE] == 200:
            CLIENT_LOGGER.debug(f'Проверка сообщения прошла успешно.')
            return '200 : ok'
        return f'400 : {message["error"]}'
    raise ReqFieldMissingError(RESPONSE)


def main():
    try:
        CLIENT_LOGGER.info(f'Начало работы функции main. Проверка указанных параметров')
        server_address = sys.argv[1]
        server_port = int(sys.argv[2])
        if server_port < 1024 or server_port > 65535:
            raise ValueError
    except IndexError:
        server_address = DEFAULT_IP_ADDRESS
        server_port = DEFAULT_PORT
        CLIENT_LOGGER.info(f'Установлены порт и адрес по умолчанию: {DEFAULT_IP_ADDRESS}/{DEFAULT_PORT}')
    except ValueError:
        CLIENT_LOGGER.info(f'Ошибка указания адреса или порта для соединения')
        sys.exit(1)

    try:
        transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        transport.connect((server_address, server_port))
        message_to_server = create_presence()
        send_message(transport, message_to_server)
        answer = action_with_server_msg(get_message(transport))
        CLIENT_LOGGER.info(f'Принят ответ от сервера {answer}')
        # print(answer)
    except json.JSONDecodeError:
        CLIENT_LOGGER.error('Не удалось декодировать полученную Json строку.')
    except ReqFieldMissingError as missing_error:
        CLIENT_LOGGER.error(f'В ответе сервера отсутствует необходимое поле '
                            f'{missing_error.missing_field}')
    except ConnectionRefusedError:
        CLIENT_LOGGER.critical(f'Не удалось подключиться к серверу {server_address}:{server_port}, '
                               f'конечный компьютер отверг запрос на подключение.')


if __name__ == '__main__':
    main()
