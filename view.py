def input_data() -> list[str]:
    lst = ['' for i in range(4)]
    lst[0] = input("Введите Фамилию: ")
    lst[1] = input("Введите Имя: ")
    lst[2] = input("Введите номер телефона: ")  # необходима валидация, чтобы номер был в формате х-ххх-ххх-хх-хх
    lst[3] = input("Введите комментарий: ")
    return lst


def print_data(in_data: str):
    print(in_data)


def input_number() -> str:
    num = input('Введите номер: ')
    num = num.replace('-', '')
    num = num.replace(' ', '')
    return num


def input_choose(message: str = 'Ваш выбор > ') -> str:
    return int(input(message))


def print_choose_action_menu():
    print("Выберите - что хотите сделать: "
          "\n1 - Поиск по Фамилии или Имени "
          "\n3 - Добавить запись в телефонную книгу "
          "\n4 - Поиск по телефону "
          "\n5 - Удаление запись из телефонной книги "
          "\n6 - Выход\n ")
