def input_data() -> list [str]:
    lst=['' for i in range(4)]
    lst[0] = input("Введите Фамилию: ")
    lst[1] = input("Введите Имя: ")
    lst[2] = input("Введите номер телефона: ") # необходима валидация, чтобы номер был в формате х-ххх-ххх-хх-хх
    lst[3] = input("Введите комментарий: ")
    return lst

def print_data(in_data: str):
    print(in_data)

def input_number() -> str:
    num = input('Введите номер: ')
    num = num.replace('-', '')
    num = num.replace(' ', '')
    return num



# def convert_list_to_str(input_array: list [str]) -> str:
#     res = ''
#     for i in input_array:
#         res += i + ';'
#     return res
