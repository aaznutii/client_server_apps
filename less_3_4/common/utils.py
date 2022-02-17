
import json
from less_3_4.common.variables import MAX_PACKAGE_LENGTH, DEFAULT_ENCODING

def get_message(client):
    response = client.recv(MAX_PACKAGE_LENGTH)
    if isinstance(response, bytes):
        response = response.decode(DEFAULT_ENCODING)
        if isinstance(response, str):
            json_response = json.loads(response)
            if isinstance(json_response, dict):
                return json_response
            raise ValueError
        raise ValueError
    raise ValueError


def send_message(sock, message):
    json_message = json.dumps(message)
    json_message = json_message.encode(DEFAULT_ENCODING)
    sock.send(json_message)