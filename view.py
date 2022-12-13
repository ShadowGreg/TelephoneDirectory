
def Input_tel():
    telephone = input("Введите номер телефона: ")
    return telephone


def print_data(in_data: str):
    print(in_data)


def convert_list_to_str(input_array: list):
    rez = ''
    for i in input_array:
        rez += i + ';'
    rez=rez[:-1]
    return rez

