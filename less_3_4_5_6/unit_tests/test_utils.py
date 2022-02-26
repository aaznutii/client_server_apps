import json
import os
import sys
import unittest
# from unittest.mock import patch
sys.path.append(os.path.join(os.getcwd(), '..'))
from common.variables import RESPONSE, ERROR, USER, ACCOUNT_NAME, ACTION, TIME, PRESENCE, DEFAULT_ENCODING
from common.utils import get_message, send_message


class TestSocket:

    def __init__(self, test_dict):
        self.test_dict = test_dict
        self.encoded_msg = None
        self.received_msg = None

    def send(self, msg_to_send):
        json_test_msg = json.dumps(self.test_dict)
        self.encoded_msg = json_test_msg.encode(DEFAULT_ENCODING)
        self.received_msg = msg_to_send

    def recv(self, any):
        json_test_msg = json.dumps(self.test_dict)
        return json_test_msg.encode(DEFAULT_ENCODING)


class TestUtils(unittest.TestCase):

    test_dict_send = {
        ACTION: PRESENCE,
        TIME: 1.1,
        USER:{
            ACCOUNT_NAME: ACCOUNT_NAME
        }
    }
    test_dict_recv_ok = {RESPONSE: 200}
    test_dict_recv_err = {RESPONSE: 400, ERROR: 'PRESENCE IS INVALID'}

    def test_send_msg_wrong(self):
        test_socket = TestSocket(self.test_dict_send)
        send_message(test_socket, self.test_dict_send)
        self.assertRaises(TypeError, send_message, 'wrong_dict')

    def test_send_msg_ok(self):
        test_socket = TestSocket(self.test_dict_send)
        send_message(test_socket, self.test_dict_send)
        self.assertEqual(test_socket.encoded_msg, test_socket.received_msg)

    def test_get_msg(self):
        test_socket_ok = TestSocket(self.test_dict_recv_ok)
        self.assertEqual(get_message(test_socket_ok), self.test_dict_recv_ok)

    def test_get_msg_err(self):
        test_socket_err = TestSocket(self.test_dict_recv_err)
        self.assertEqual(get_message(test_socket_err), self.test_dict_recv_err)


if __name__ == '__main__':
    unittest.main()