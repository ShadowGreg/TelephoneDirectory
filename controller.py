import database
import view
import funcs

CHOICE_SEARCH = 1
CHOICE_PRINT_DIRECTORY = 2
CHOICE_ADD_CONTACT = 3
CHOICE_DELETE_CONTACT = 4
CHOICE_MAIN_MENU = 5
CHOICE_EXIT = 6


def choose_an_action(exit_choice=False):
    view.print_choose_action_menu()
    while not exit_choice:
        choice = view.input_choose()
        if choice == CHOICE_SEARCH:
            phone_data = search_by_input_data()
            print_array_data_from(phone_data)
        if choice == CHOICE_PRINT_DIRECTORY:
            data_base = funcs.get_data_from_bd(database.read_from_file())
            print_array_data_from(data_base)
        if choice == CHOICE_ADD_CONTACT:
            new_line_data = funcs.add_new_line_in_bd(view.input_data())
            database.write_to_csv(new_line_data)
            database.write_to_txt(new_line_data)
        if choice == CHOICE_DELETE_CONTACT:
            full_data = funcs.delete_line_fom_bd(view.input_phone_number())
            database.full_rewrite_csv(full_data)
            database.full_rewrite_txt(full_data)
        if choice == CHOICE_MAIN_MENU:
            view.print_choose_action_menu()
        if choice == CHOICE_EXIT:
            exit_choice = True


def print_array_data_from(input_data: list[list[str]]):
    for item in input_data:
        view.print_data(item)


def search_by_input_data() -> list[list[str]]:
    return funcs.search_by_phone(
        view.input_phone_number(),
        funcs.get_data_from_bd(database.read_from_file()))
