def get_data_from_bd(file_data: str) -> list[list[str]]:
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
        file_data = file_data.split('  ')
        for word in file_data:
            if word != '':
                s = word.split(';')
                lst.append(s)
        return lst


def search_by_phone(input_phone_number: str, input_array: list) -> list:
    output_records = []
    for record_line in input_array:
        if input_phone_number in record_line[2]:
            output_records.append(record_line)
    return output_records


def add_new_line_in_bd(input_method):
    return input_method


def delete_line_fom_bd(input_phone_number: str, input_array: list) -> list:
    for i in range(len(input_array) + 1):
        if input_array[i][2] == input_phone_number:
            input_array.pop(i)
    return input_array
