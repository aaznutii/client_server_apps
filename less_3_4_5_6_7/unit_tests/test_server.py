import os
import sys
import unittest
# from unittest.mock import patch
sys.path.append(os.path.join(os.getcwd(), '..'))
from server import action_with_client_msg
from common.variables import RESPONSE, ERROR, USER, ACCOUNT_NAME, ACTION, TIME, PRESENCE

class TestServer(unittest.TestCase):

    err_dict = {RESPONSE: 400, ERROR: 'PRESENCE IS INVALID'}

    ok_dict = {RESPONSE: 200}

    def setUp(self):
        # Выполнить настройку тестов (если необходимо)
        pass

    def tearDown(self):
        # Выполнить завершающие действия (если необходимо)
        pass

    def test_ok_check(self):
        self.assertEqual(action_with_client_msg(
            {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: "Guest"}}), self.ok_dict)

    def test_no_action(self):
        self.assertEqual(action_with_client_msg(
            {TIME: 1.1, USER: {ACCOUNT_NAME: "Guest"}}), self.err_dict)


    def test_wrong_action(self):
        self.assertEqual(action_with_client_msg(
            {ACTION: 'Wrong', TIME: 1.1, USER: {ACCOUNT_NAME: "Guest"}}), self.err_dict)

    def test_no_time(self):
        self.assertEqual(action_with_client_msg(
            {ACTION: PRESENCE, USER: {ACCOUNT_NAME: "Guest"}}), self.err_dict)

    def test_no_user(self):
        self.assertEqual(action_with_client_msg(
            {ACTION: PRESENCE, TIME: 1.1}), self.err_dict)

    def test_unknow_user(self):
        self.assertEqual(action_with_client_msg(
            {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: "Any"}}), self.err_dict)

if __name__ == '__main__':
    unittest.main()