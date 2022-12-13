def write_to_csv(a,b,c,d: str, input_file_name: str = 'bp.csv'):
    with open(input_file_name, "a", encoding='utf-8') as data:
        data.write(f'{a};{b};{c};{d}\n')


def write_to_txt(a,b,c,d: str, input_file_name: str = 'bp.txt'):
    with open(input_file_name, "a", encoding='utf-8') as data:
        data.write(
            f'Фамилия: {b}'
            f'\n\nИмя: {a}'
            f'\n\nНомер телефона: {c}'
            f'\n\nОписание: {d} \n\n\n')


def read_from_file(input_file_name: str = 'bp.csv'):
    with open(input_file_name, "r", encoding='utf-8') as data:
        file_data = data.read()
    return file_data


# TODO add delete
