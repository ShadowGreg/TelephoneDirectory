import database
import view
import funcs
import start_data
import click
from exception import logging
from os import system, name

CHOICE_SEARCH = 1
CHOICE_PRINT_DIRECTORY = 2
CHOICE_ADD_CONTACT = 3
CHOICE_DELETE_CONTACT = 4
CHOICE_MAIN_MENU = 5
CHOICE_EXIT = 6


def choose_an_action(exit_choice=False):
    checking_existence_bd()
    view.print_choose_action_menu()
    while not exit_choice:
        choice = view.input_choose()
        if choice == CHOICE_SEARCH:
            search()
        if choice == CHOICE_PRINT_DIRECTORY:
            print_directory()
        if choice == CHOICE_ADD_CONTACT:
            add_contact()
        if choice == CHOICE_DELETE_CONTACT:
            delete_contact()
        if choice == CHOICE_MAIN_MENU:
            clear()
            view.print_choose_action_menu()
        if choice == CHOICE_EXIT:
            exit_choice = True


def search():
    try:
        phone_data = search_by_info()
        print_array_data_from(phone_data)
    except Exception as e:
        logging.debug(e)


def print_directory():
    try:
        data_base = funcs.get_data_from_bd(database.read_from_file())
        print_array_data_from(data_base)
    except Exception as e:
        logging.debug(e)


def add_contact():
    try:
        new_line_data = funcs.add_new_line_in_bd(view.input_data())
        database.write_to_csv(new_line_data)
        database.write_to_txt(new_line_data)
    except Exception as e:
        logging.debug(e)


def delete_contact():
    try:
        full_data = funcs.delete_line_fom_bd(
            view.input_info(),
            funcs.get_data_from_bd(database.read_from_file()))
        database.delete_csv()
        database.delete_txt()
        for item in full_data:
            database.write_to_txt(item)
            database.write_to_csv(item)
    except Exception as e:
        logging.debug(e)


def print_array_data_from(input_data: list[list[str]]):
    try:
        if not input_data:
            view.print_not_found()
        else:
            for item in input_data:
                view.print_data(item)
    except Exception as e:
        logging.debug(e)


def search_by_info() -> list[list[str]]:
    try:
        return funcs.search_by_input_info(
            view.input_info(),
            funcs.get_data_from_bd(database.read_from_file()))
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



