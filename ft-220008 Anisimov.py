import random
import logging
from colorama import Fore

# Настройка логирования
logging.basicConfig(filename='game.log', level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')
def get_number(message, min_value=1, max_value=None):
    """
    Функция для получения числа от пользователя.

    Args:
        message: Текстовое сообщение для пользователя.
        min_value: Минимальное допустимое значение.
        max_value: Максимальное допустимое значение.

    Returns:
        Введенное число.
    """

    while True:
        try:
            number = int(input(message))
            if min_value is not None and number < min_value:
                logging.warning('Введено число меньше допустимого.')
                print(Fore.YELLOW + f'Введите число от {min_value} до {max_value}.')
                continue
            if max_value is not None and number > max_value:
                logging.warning('Введено число больше допустимого.')
                print(Fore.YELLOW + f'Введите число от {min_value} до {max_value}.')
                continue
            return number
        except ValueError:
            logging.error('Введено некорректное число.')
            print(Fore.RED + 'Введите целое число.')
        except TypeError:
            logging.error('Введено пустое значение.')
            print(Fore.RED + 'Введите число.')


def main():
    """
    Основная функция игры.
    """