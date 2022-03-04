
import logging

# Базовые константы
DEFAULT_PORT = 7777

DEFAULT_IP_ADDRESS = '127.0.0.1'

MAX_CONNECTIONS = 5

MAX_PACKAGE_LENGTH = 1024

DEFAULT_ENCODING = 'utf-8'


# Ключи протоколов

ACTION = 'action'
TIME = 'time'
USER = 'user'
ACCOUNT_NAME = 'account_name'
SENDER = 'from'
DESTINATION = 'to'

# Другие ключи
PRESENCE = 'presence'
RESPONSE = 'response'
ERROR = 'error'
RESPONSE_DEFAULT_IP_ADDRESS = 'response_default_ip_address'
EXIT = 'exit'

# Установить уровень логирования

LOGGING_LEVEL_SERVER = logging.DEBUG
LOGGING_LEVEL_CLIENT = logging.DEBUG

MESSAGE = 'message'
MESSAGE_TEXT = 'mess_text'

# Словари - ответы:
# 200
RESPONSE_200 = {RESPONSE: 200}
# 400
RESPONSE_400 = {
    RESPONSE: 400,
    ERROR: None
}
