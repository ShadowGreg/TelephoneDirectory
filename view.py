def input_data() -> list[str]:
    lst = ['' for i in range(4)]
    lst[0] = input_surname()
    lst[1] = input_name()
    lst[2] = input_info()
    lst[3] = input_comment()
    print_separator()
    return lst


def input_surname():
    return input("Введите Фамилию: ")


def input_name():
    return input("Введите Имя: ")


def input_info():
    return input("Искать: ")


def input_comment():
    return input("Введите комментарий: ")


def print_data(in_data: str):
    print(in_data)


def input_number() -> str:
    num = input('Введите номер: ')
    num = num.replace('-', '')
    num = num.replace(' ', '')
    return num


def input_choose(message: str = f'Ваш выбор (Что бы повторить меню - 5) > ') -> int:
    return int(input(message))


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

