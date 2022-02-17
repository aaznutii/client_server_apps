import os
import sys
import unittest
from unittest.mock import patch
sys.path.append(os.path.join(os.getcwd(), ' '))
from less_3_4.client import create_presance, action_with_server_msg, main
from less_3_4.common.variables import RESPONSE, ERROR, USER, ACCOUNT_NAME, ACTION, TIME, PRESENCE

class Test_client(unittest.TestCase):

    def setUp(self):
        # Выполнить настройку тестов (если необходимо)
        pass

    def tearDown(self):
        # Выполнить завершающие действия (если необходимо)
        pass

    def test_def_create_presance(self):
        test = create_presance()
        test[TIME] = 1.1
        self.assertEqual(test, {ACTION: PRESENCE, TIME: 1.1, USER:{ACCOUNT_NAME: 'Guest'}})

    def test_def_action_with_server_msg_200(self):
        self.assertEqual(action_with_server_msg({RESPONSE: 200}), '200 : ok')

    def test_def_action_with_server_msg_400(self):
        self.assertEqual(action_with_server_msg({RESPONSE: 400, ERROR: 'PRESENCE IS INVALID'}), '400 : PRESENCE IS INVALID')

    def test_def_action_with_server_msg_no_response(self):
        self.assertRaises(ValueError, action_with_server_msg, {ERROR: 'PRESENCE IS INVALID'})

#      Добавить __main__
    @patch.object(sys, 'argv', ['client.py'])
    def test_main_ConnectionRefusedError(self):
        self.assertRaises(ConnectionRefusedError, main)


if __name__ == '__main__':
    unittest.main()