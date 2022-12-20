import database
import view
import funcs
import start_data
from exception import logging
from os import system, name
from logger_file import log_info


def choose_an_action(exit_choice=False):
    try:
        func_dict = {
            1: lambda: search(),
            2: lambda: print_directory(),
            3: lambda: add_contact(),
            4: lambda: delete_contact(),
            5: lambda: print_main_menu(),
            6: lambda: checking_exit()
        }
        checking_existence_bd()
        view.print_choose_action_menu()
        while not exit_choice:
            choice = view.input_choose()
            if func_dict.get(choice, None) is not None:
                func_dict[choice]()
    except Exception as e:
        logging.debug(e)


def print_main_menu():
    try:
        clear()
        view.print_choose_action_menu()
    except Exception as e:
        logging.debug(e)


def search():
    try:
        phone_data = search_by_info()
        print_array_data_from(phone_data)
        log_info(f'Searched info: {phone_data}', 'search')
    except Exception as e:
        logging.debug(e)


def print_directory():
    try:
        data_base = funcs.get_data_from_bd(database.read_from_file())
        print_array_data_from(data_base)
        log_info(f'Printed database', 'print_directory')
    except Exception as e:
        logging.debug(e)


def add_contact():
    try:
        new_line_data = funcs.add_new_line_in_bd(view.input_data())
        database.write_to_csv(new_line_data)
        database.write_to_txt(new_line_data)
        log_info(f'Added record: {new_line_data}', 'add_contact')
    except Exception as e:
        logging.debug(e)


def delete_contact():
    try:
        full_data = funcs.delete_much_contact(view.input_data(), funcs.get_data_from_bd(database.read_from_file()))
        database.delete_csv()
        database.delete_txt()
        for item in full_data:
            database.write_to_txt(item)
            database.write_to_csv(item)
        log_info(f'Delete record: {item}', 'delete_contact')
    except Exception as e:
        logging.debug(e)


def print_array_data_from(input_data: list[list[str]]):
    try:
        if not input_data:
            view.print_not_found()
        else:
            for item in input_data:
                view.print_data(item)
        log_info(f'Print dataForm: {item}', 'print_array_data_form')
    except Exception as e:
        logging.debug(e)


def search_by_info() -> list[list[str]]:
    try:
        return funcs.search_by_input_info(
            view.input_info(),
            funcs.get_data_from_bd(database.read_from_file()))
        log_info(f'Searched info:', 'search_by_info')
    except Exception as e:
        logging.debug(e)


def checking_existence_bd():
    try:
        if not database.read_from_file():
            for item in start_data.start_data:
                database.write_to_txt(item)
                database.write_to_csv(item)
                
    except Exception as e:
        logging.debug(e)


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def checking_exit():
    raise SystemExit
