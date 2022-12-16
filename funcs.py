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


def search_by_phone(input_phone_number: str, input_array: list[list[str]]) -> list[list[str]]:
    try:
        output_records = []
        for record_line in input_array:
            if input_phone_number in record_line[2]:
                output_records.append(record_line)
        return output_records
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

