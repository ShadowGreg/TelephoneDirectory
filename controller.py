import database
import view
import funcs


def choose_an_action(case_flag=True):
    view.print_choose_action_menu()
    while case_flag:
        choice = view.input_choose()
        match choice:
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                case_flag = False


choose_an_action()
