def input_data() -> list [str]:
    lst=['' for i in range(4)]
    lst[0] = input("Введите Фамилию: ")
    lst[1] = input("Введите Имя: ")
    lst[2] = input("Введите номер телефона: ") # необходима валидация, чтобы номер был в формате х-ххх-ххх-хх-хх для того, чтобы он красиво отображался в файле
    lst[3] = input("Введите комментарий: ")
    return lst

def input_number() -> str:
    num = input('Введите номер: ')
    num = num.replace('-', '')
    num = num.replace(' ', '')
    return num

def input_surname() -> str:
    surname = input('Введите Фамилию: ')
    return surname

def input_name() -> str:
    surname = input('Введите Имя: ')
    return surname

def input_comment() -> str:
    surname = input('Введите Комментарий: ')
    return surname

def print_data(in_data):
    print(in_data)

