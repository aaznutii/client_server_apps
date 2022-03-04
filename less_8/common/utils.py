
import json
import sys
sys.path.append('../')

from logs.log_func_actions import log
from logs.errors import IncorrectDataRecivedError, NonDictInputError
from common.variables import MAX_PACKAGE_LENGTH, DEFAULT_ENCODING

def get_message(client):
    response = client.recv(MAX_PACKAGE_LENGTH)
    if isinstance(response, bytes):
        response = response.decode(DEFAULT_ENCODING)
        if isinstance(response, str):
            json_response = json.loads(response)
            if isinstance(json_response, dict):
                return json_response
            raise IncorrectDataRecivedError
        raise ValueError
    raise IncorrectDataRecivedError


def send_message(sock, message):
    """
    Утилита кодирования и отправки сообщения
    принимает словарь и отправляет его
    :param sock:
    :param message:
    :return:
    """
    if not isinstance(message, dict):
        raise NonDictInputError
    js_message = json.dumps(message)
    encoded_message = js_message.encode(DEFAULT_ENCODING)
    sock.send(encoded_message)