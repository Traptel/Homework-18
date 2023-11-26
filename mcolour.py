"""
Модуль, що містить функції для створення кольорових
повідомлень та стилізації тексту.
"""
colour = {
    'red': '31m',
    'black': '30m',
    'green': '32m',
    'yellow': '33m',
    'blue': '34m',
    'purpure': '35m',
    'biruza': '36m',
    'white': '37m'
}


def color_text(text: str, colour_name: str) -> str:
    """
    Функція змінює колір тексту.

    :param text: Текст, якому потрібно змінити колір.
    :param colour_name: Назва кольору.

    :return: Тексту з вказаним кольором.
    """
    coloured_txt = '\033[' + colour_name + text + '\033[0m'
    return coloured_txt


def styled(text: str, code: str = "3m") -> str:
    """
    Функція змінює стиль тексту.

    :param text: Текст, який потрібно стилізувати.
    :param code: Код стилю тексту.

    :return: Стилізований текст.
    """
    clean_style_code = '\033[0m'
    styled_txt = f'\033[{code}{text}{clean_style_code}'
    return styled_txt


def error_message(message: str) -> str:
    """
    Функція повертає рядок тексту помилки з червоним кольором.

    :param message: Повідомлення про помилку.

    :return: Рядок тексту помилки.
    """
    status = "ERROR"
    error = color_text(f"{status:<8} ", colour['red'])
    _message = color_text(message, colour['yellow'])
    err_message = error + _message
    return err_message


def warning_message(message: str) -> str:
    """
    Функція повертає рядок тексту попередження з жовтим кольором.

    :param message: Попередження.

    :returns: Рядок тексту попередження.
    """
    status = "WARNING"
    warn = color_text(f"{status:<8} ", colour['yellow'])
    _message = color_text(message, colour['biruza'])
    warn_message = warn + _message
    return warn_message


def info_message(message: str) -> str:
    """
    Функція повертає рядок тексту з інформацією з фіолетовим кольором.

    :param message: Інформація.

    :return: Рядок тексту з інформацією.
    """
    status = "INFO"
    info = color_text(f"{status:<8} ", colour['purpure'])
    info_message = info + message
    return info_message


def change_style_text(text: str, text_style: str = "", text_color: str = "", background_color: str = " ") -> str:
    """
    Функція стилізує параметрами тексту, змінює стиль, колір тексту та фон.

    :param text: Текст для стилізації.
    :param text_style: Стиль тексту.
    :param text_color: Колір тексту.
    :param background_color: Колір фону.

    :return: Повертає стилізований текст.
    """

    style = f'\033[{text_style};{text_color};{background_color}m'
    clean = '\033[0m'
    styled_text = f'{style}{text}{clean}'
    return styled_text


"""
Example:
s = "\033[3m"
c = "\033[33m"
f  = "\033[41m";
clean = "\033[0m"
pattern = f"{s}{c}{f}{txt}{clean}"
"""

if __name__ == "__main__":
    print(warning_message("ups i did sit again"))
    print(error_message("wrong way"))
    print(info_message("thanks for info"))
