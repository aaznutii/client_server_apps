
import unittest
from less_3.common.utils import get_message


# def get_message(client):
#     response = client.recv(MAX_PACKAGE_LENGTH)
#     if isinstance(response, bytes):
#         response = response.decode(DEFAULT_ENCODING)
#         if isinstance(response, str):
#             json_response = json.loads(response)
#             if isinstance(json_response, dict):
#                 return json_response
#             raise ValueError
#         raise ValueError
#     raise ValueError


class Test_get_message(unittest.TestCase):

    def setUp(self):
        # Выполнить настройку тестов (если необходимо)
        pass

    def tearDown(self):
        # Выполнить завершающие действия (если необходимо)
        pass

    def test_isinstance(self):
        client = ''
        """используем функцию assertIsInstance"""
        self.assertIsInstance(get_message(client), dict)


if __name__ == '__main__':
    unittest.main()