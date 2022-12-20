from exception import logging


def get_data_from_bd(file_data: str) -> list[list[str]]:
    try:
        file_data = file_data.replace('-', '')
        file_data = file_data.replace(' ', '')
        file_data = file_data.replace('\n', ' ')
        lst = []
        if '  ' in file_data:
            file_data = file_data.split('  ')
            for word in file_data:
                if word != '':
                    s = word.split(' ')
                    lst.append(s)
            return lst
        elif ';' in file_data:
            file_data = file_data.split(' ')
            for word in file_data:
                if word != '':
                    s = word.split(';')
                    lst.append(s)
            return lst
    except Exception as e:
        logging.debug(e)


def search_by_input_info(input_info: str, input_array: list[list[str]]) -> list[list[str]]:
    try:
        output = []
        for hi_level_item in input_array:
            for low_level_item in hi_level_item:
                if input_info in low_level_item:
                    output.append(hi_level_item)
        return output
    except Exception as e:
        logging.debug(e)


def add_new_line_in_bd(input_method):
    return input_method


def delete_line_fom_bd(input_phone_number: str, input_array: list[list[str]]) -> list[list[str]]:
    try:
        output_array = []
        PHONE_INDEX = 2
        for item in input_array:
            if item[PHONE_INDEX] != input_phone_number:
                output_array.append(item)
        return output_array
    except Exception as e:
        logging.debug(e)


def delete(input_array: list[list[str]]) -> list[list[str]]:
    try:
        output_array = []
        COUNT = 0
        SURNAME = input('Введите Фамилию для удаления: ')
        for item in input_array:
            if SURNAME == item[0]:
                COUNT += 1
        if COUNT == 1:
            for item in input_array:
                if SURNAME != item[0]:
                    output_array.append(item)
                else:
                    print(f'Контакт {item} удалён')
        else:
            print('Найдены контакты с одинаковой фамилией:')
            for item in input_array:
                if SURNAME == item[0]:
                    print(item)
            COUNT = 0
            NAME = input('Введите Имя для удаления: ')
            for item in input_array:
                if SURNAME == item[0] and NAME == item[1]:
                    COUNT += 1
            print(COUNT)
            if COUNT == 1:
                for item in input_array:
                    if SURNAME != item[0] or NAME != item[0]:
                        output_array.append(item)
                    else:
                        print(f'Контакт {item} удалён')
            else:
                print('Найдены контакты с одинаковыи фамилией и именем:')
                for item in input_array:
                    if SURNAME == item[0] and NAME == item[1]:
                        print(item)
                COUNT = 0
                NUMBER = input('Введите номер для удаления: ')
                for item in input_array:
                    if SURNAME == item[0] and NAME == item[1] and NUMBER == item[2]:
                        COUNT += 1
                print(COUNT)
                if COUNT == 1:
                    for item in input_array:
                        if SURNAME != item[0] or NAME != item[1] or NUMBER != item[2]:
                            output_array.append(item)
                        else:
                            print(f'Контакт {item} удалён')
                else:
                    print('Найдены контакты с одинаковыи фамилией, именем и номером:')
                    for item in input_array:
                        if SURNAME == item[0] and NAME == item[1] and NUMBER == item[2]:
                            print(item)
                    COMMENT = input('Введите комментарий для удаления: ')
                    for item in input_array:
                        if SURNAME != item[0] or NAME != item[1] \
                                   or NUMBER != item[2] or COMMENT != item[3]:
                            output_array.append(item)
                        else:
                            print(f'Контакт {item} удалён')
        return output_array
    except Exception as e:
        logging.debug(e)
