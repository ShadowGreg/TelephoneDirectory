test_data = [
    ['Сидоров', 'Иван', '89062348976', 'сотовый'],
    ['Антонов', 'Михаил', '89362348976', ' '],
    ['Емельянов', 'Максим', '89066458976', 'мобильный'],
    ['Петров', 'Владислав', '89062342345', ' '],
]


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


for i in test_data:
    write_to_txt(i)
    write_to_csv(i)
