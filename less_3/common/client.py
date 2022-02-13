import json
import socket
import sys
import time

from less_3.common.utils import send_message, get_message
from less_3.common.variables import ACTION, PRESENCE, TIME, USER, ACCOUNT_NAME, RESPONSE, DEFAULT_IP_ADDRESS, \
    DEFAULT_PORT

def create_presance(account_name='Guest'):
    result = {
        ACTION: PRESENCE,
        TIME: time.time(),
        USER:{
            ACCOUNT_NAME: account_name
        }
    }
    return result

def action_with_server_msg(message):
    if RESPONSE in message:
        if message[RESPONSE] == 200:
            return '200 : ok'
        return f'400 : {message}'
    raise ValueError


def main():
    try:
        server_address = sys.argv[1]
        server_port = int(sys.argv[2])
        if server_port < 1024 or server_port > 65535:
            raise ValueError
    except IndexError:
        server_address = DEFAULT_IP_ADDRESS
        server_port = DEFAULT_PORT
    except ValueError:
        print('Ошибка указания адреса или порта для соединения')
        sys.exit(1)

    transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    transport.connect((server_address, server_port))
    message_to_server = create_presance()
    send_message(transport, message_to_server)
    try:
        answer = action_with_server_msg(get_message(transport))
        print(answer)
    except (ValueError, json.JSONDecodeError):
        print('Не удалось прочитать сообщение сервера')

if __name__ == '__main__':
    main()