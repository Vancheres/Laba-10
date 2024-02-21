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
    # Запрашиваем у пользователя N и k
    logging.info('Начало игры.')
    n = get_number('Введите N (максимальное число): ', 1, None)
    k = get_number('Введите k (количество попыток): ', 1, None)

    # Загадываем число
    logging.info('Загадываем число...')
    secret_number = random.randint(1, n)

    # Цикл игры
    for i in range(k):
        # Запрашиваем число у пользователя
        logging.info('Попытка {} из {}.'.format(i + 1, k))
        guess = get_number('Введите число: ', 1, n)

        # Сравниваем с загаданным числом
        if guess == secret_number:
            logging.info('Число угадано!')
            print(Fore.GREEN + 'Вы угадали!')
            break
        elif guess < secret_number:
            logging.info('Введенное число меньше.')
            print(Fore.YELLOW + 'Загаданное число больше.')
        else:
            logging.info('Введенное число больше.')
            print(Fore.YELLOW + 'Загаданное число меньше.')

    # Выводим результат игры
    if i == k - 1:
        logging.info('Попытки закончились.')
        print(Fore.RED + 'Попытки закончились. Загаданное число было {}.'.format(secret_number))


if __name__ == '__main__':
    main()