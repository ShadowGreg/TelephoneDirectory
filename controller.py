import database
import view
import funcs


def choose_an_action(case_flag=True):
    view.print_choose_action_menu()
    while case_flag:
        choice = view.input_choose()
        if choice == 1:
            phone_data = search_by_input_data()
            print_array_data_from(phone_data)
        if choice == 2:
            data_base = funcs.get_data_from_bd(database.read_from_file())
            print_array_data_from(data_base)
        if choice == 3:
            new_line_data = funcs.add_new_line_in_bd(view.input_data())
            database.write_to_csv(new_line_data)
            database.write_to_txt(new_line_data)
        if choice == 4:
            full_data = funcs.delete_line_fom_bd(view.input_phone_number())
            database.full_rewrite_csv(full_data)
            database.full_rewrite_txt(full_data)
        if choice == 5:
            view.print_choose_action_menu()
        if choice == 6:
            case_flag = False


def print_array_data_from(input_data: list[list[str]]):
    for item in input_data:
        view.print_data(item)


def search_by_input_data() -> list[list[str]]:
    return funcs.search_by_phone(
        view.input_phone_number(),
        funcs.get_data_from_bd(database.read_from_file()))
