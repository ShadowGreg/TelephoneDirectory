from exception import logging


def input_data() -> list[str]:
    try:
        lst = ['' for i in range(4)]
        lst[0] = input_surname()
        lst[1] = input_name()
        lst[2] = input_telephone()
        lst[3] = input_comment()
        print_separator()
        return lst
    except Exception as e:
        logging.debug(e)


def input_surname():
    try:
        return input("Введите Фамилию: ")
    except Exception as e:
        logging.debug(e)


def input_name():
    try:
        return input("Введите Имя: ")
    except Exception as e:
        logging.debug(e)


def input_telephone():
    try:
        return input("Введите телефон: ")
    except Exception as e:
        logging.debug(e)


def input_comment():
    try:
        return input("Введите комментарий: ")
    except Exception as e:
        logging.debug(e)


def input_info():
    try:
        return input("Искать: ")
    except Exception as e:
        logging.debug(e)


def print_data(in_data: str):
    try:
        print(in_data)
    except Exception as e:
        logging.debug(e)


def input_number() -> str:
    try:
        num = input('Введите номер: ')
        num = num.replace('-', '')
        num = num.replace(' ', '')
        return num
    except Exception as e:
        logging.debug(e)


def input_choose(message: str = f'Ваш выбор (Что бы повторить меню - 5) > ') -> int:
    try:
        return int(input(message))
    except Exception as e:
        logging.debug(e)


def print_choose_action_menu():
    print("Выберите - что хотите сделать: "
          "\n1 - Поиск записи по номеру телефона "
          "\n2 - Распечатать телефонную книгу "
          "\n3 - Добавить запись в телефонную книгу "
          "\n4 - Удаление запись из телефонной книги "
          "\n5 - Главное меню "
          "\n6 - Выход\n ")


def print_data(input_array: list):
    print(f"Фамилия: {input_array[0]}")
    print(f"Имя: {input_array[1]}")
    print(f"Номер телефона: {input_array[2]}")
    print(f"Комментарий: {input_array[3]}")
    print_separator()


def print_not_found():
    print('Контакт не найден, попробуйте ещё раз')
    print_separator()


def print_separator():
    print('---------------------')
