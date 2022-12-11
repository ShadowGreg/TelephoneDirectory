def input_data():
    fio = input("Введите ФИО: ")
    telephone = input("Введите номер телефона: ")
    comment = input("Введите комментарий: ")
    return fio, telephone, comment


def print_data(in_data: str):
    print(in_data)


def convert_list_to_str(input_array: list):
    rez = ''
    for i in input_array:
        rez += i + ';'
    return rez
