import database
import view
import funcs


def choose_an_action(case_flag=True):
    view.print_choose_action_menu()
    while case_flag:
        choice = view.input_choose()
        if choice == 1:
            phone_data = funcs.search_by_phone(view.input_phone_number())
            view.print_data(phone_data)
        if choice == 2:
            for item in funcs.get_data_from_bd():
                view.print_data(item)
        if choice == 3:
            new_line_data = funcs.add_new_line_in_bd(view.input_data())
            database.write_to_csv(new_line_data)
            database.write_to_txt(new_line_data)
        if choice == 4:
            full_data = funcs.delete_line_fom_bd(view.input_phone_number())
            database.full_rewrite_csv(full_data)
            database.full_rewrite_txt(full_data)
        if choice == 5:
            case_flag = False


choose_an_action()
