def write_to_csv(input_data: list, input_file_name: str = 'bp.csv'):
    with open(input_file_name, "a", encoding='utf-8') as data:
        data.write(f'{input_data[0]};{input_data[1]};{input_data[2]};{input_data[3]}\n')


def write_to_txt(input_data: list[str], input_file_name: str = 'bp.txt'):
    with open(input_file_name, "a", encoding='utf-8') as data:
        data.write(
            f'{input_data[0]}'
            f'\n{input_data[1]}'
            f'\n{input_data[2]}'
            f'\n{input_data[3]}\n\n')


def read_from_file(input_file_name: str = 'bp.csv') -> str:
    if '.txt' in input_file_name:
        with open(input_file_name, "r", encoding='utf-8') as data:
            file_data = data.read()
            return file_data
    elif '.csv' in input_file_name:
        with open(input_file_name, "r", encoding='utf-8') as data:
            file_data = data.read()
            return file_data


# TODO функцию полной перезаписи базы

def full_rewrite_csv(input_data: list, input_file_name: str = 'bp.csv'):
    with open(input_file_name, "r", encoding='utf-8') as f:
        data = f.readlines()
    with open(input_file_name, "w", encoding='utf-8') as f:
        for line in data:
            if line.strip("\n") != view.input_phone_number:
                return f
            # condition for data to be deleted
            else:
                f.write(line)


def full_rewrite_txt(input_data: list[str], input_file_name: str = 'bp.txt'):
    with open(input_file_name, "r", encoding='utf-8') as f:
        data = f.readlines()
    with open(input_file_name, "w", encoding='utf-8') as f:
        for line in data:
            # condition for data to be deleted
            if line.strip("\n") == view.input_phone_number:
                f.write(line)
            else:
                return f
