
import sys
import logging
sys.path.append('../')

from logs import config_server_log
from logs import config_client_log


# проверка в наименовании модуля
if sys.argv[0].find('client'):
    # сервер
    LOGGER = logging.getLogger('server')
else:
    #  клиент
    LOGGER = logging.getLogger('client')


def log(func_to_log):
    """Функция-декоратор"""
    def log_any(*args, **kwargs):
        result = func_to_log(*args, **kwargs)
        LOGGER.debug(f'Была вызвана функция {func_to_log.__name__} c параметрами {args}, {kwargs}. '
                     f'Вызов из модуля {func_to_log.__module__}')
        return result
    return log_any
