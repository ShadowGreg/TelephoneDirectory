from exception import logging
import os
import logger_file


def write_to_csv(input_data: list[str], input_file_name: str = 'bp.csv'):
    try:
        with open(input_file_name, "a", encoding='utf-8') as data:
            data.write(f'{input_data[0]};{input_data[1]};{input_data[2]};{input_data[3]}\n')
            logger_file.log_info(f'Record {data} was written to CSV file', 'write_to_text')
    except Exception as e:
        logging.debug(e)


def write_to_txt(input_data: list[str], input_file_name: str = 'bp.txt'):
    try:
        with open(input_file_name, "a", encoding='utf-8') as data:
            data.write(
                f'{input_data[0]}'
                f'\n{input_data[1]}'
                f'\n{input_data[2]}'
                f'\n{input_data[3]}\n\n')
            logger_file.log_info(f'Record {data} was written to text file', 'write_to_text')
    except Exception as e:
        logging.debug(e)


def read_from_file(input_file_name: str = 'bp.csv') -> str:
    try:
        if '.txt' in input_file_name:
            with open(input_file_name, "r", encoding='utf-8') as data:
                file_data = data.read()
                return file_data
        elif '.csv' in input_file_name:
            with open(input_file_name, "r", encoding='utf-8') as data:
                file_data = data.read()
                return file_data
            logger_file.log_info(f'Record {file_data} was requested from database', 'read_from_file')
    except Exception as e:
        logging.debug(e)


def delete_csv(input_file_name: str = 'bp.csv'):
    try:
        os.remove(input_file_name)
    except Exception as e:
        logging.debug(e)


def delete_txt(input_file_name: str = 'bp.txt'):
    try:
        os.remove(input_file_name)
    except Exception as e:
        logging.debug(e)
