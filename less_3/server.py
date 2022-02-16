import json
import socket
import sys

from less_3.common.utils import get_message, send_message
from less_3.common.variables import ACTION, PRESENCE, ACCOUNT_NAME, USER, RESPONSE, RESPONSE_DEFAULT_IP_ADDRESS, ERROR, \
    TIME, DEFAULT_PORT, MAX_CONNECTIONS

def action_with_client_msg(message):
    if ACTION in message and message[ACTION] == PRESENCE and TIME in message and USER in message \
        and message[USER][ACCOUNT_NAME] == 'Guest':
        return {RESPONSE: 200}
    else:
        return {
            # RESPONSE_DEFAULT_IP_ADDRESS: 400,
            RESPONSE: 400,
            ERROR: 'PRESENCE IS INVALID'
        }

def main():
    try:
        if '-p' in sys.argv:
            listen_port = int(sys.argv[sys.argv.index('-p') + 1])
        else:
            listen_port = DEFAULT_PORT
        if listen_port < 1024 or listen_port > 65535:
            raise ValueError
    except IndexError:
        print('Необходимо указать номер порта после -p.')
        sys.exit(1)
    except ValueError:
        print('Может быть указано только число от 1024 до 65535')
        sys.exit(1)

    try:
        if '-a' in sys.argv:
            listen_address = sys.argv[sys.argv.index('-p') + 1]
        else:
            listen_address = ''
    except IndexError:
        print('Необходимо указать адрес ip после -a.')
        sys.exit(1)
    except ValueError:
        print('Может быть указано только число от 1024 до 65535')
        sys.exit(1)

    transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    transport.bind((listen_address, listen_port))

    transport.listen(MAX_CONNECTIONS)

    while True:
        client, client_address = transport.accept()
        try:
            msg_from_client = get_message(client)
            print(f'Получен запрос от клиента {msg_from_client}')
            response = action_with_client_msg(msg_from_client)
            send_message(client, response)
            client.close()
        except (ValueError, json.JSONDecodeError):
            print('Принято некорректное сообщение от клиента')
            client.close()


if __name__ == '__main__':
    main()