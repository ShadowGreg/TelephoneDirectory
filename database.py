def write_to_csv(input_data: list, input_file_name: str = 'bp.csv'):
    with open(input_file_name, "a", encoding='utf-8') as data:
        data.write(f'{input_data[0]};{input_data[1]};{input_data[2]};{input_data[3]}\n')


def write_to_txt(input_data: list[str], input_file_name: str = 'bp.txt'):
    with open(input_file_name, "a", encoding='utf-8') as data:
        data.write(
            f'{input_data[0]}'
            f'\n{input_data[1]}'
            f'\n{input_data[2]}'
            f'\n{input_data[3]}\n\n\n')


def read_from_file(input_file_name: str = 'bp.csv'):
    with open(input_file_name, "r", encoding='utf-8') as data:
        file_data = data.read()
        file_data = file_data.replace('-', '')
        file_data = file_data.replace('\n', ' ')
        file_data = file_data.split('   ')
        lst = []
        for word in file_data:
            s = word.split(' ')
            lst.append(s)
        print(lst)
    return file_data


# TODO функцию полной перезаписи базы

def full_rewrite_csv(in_data: list[list]):
    return 'ок'


def full_rewrite_txt(in_data: list[list]):
    return 'ок'
