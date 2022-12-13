import database
import view
import funcs


def choose_an_action():
    p = int(input("Выберите - что хотите сделать: "
                  "\n1 - Поиск по телефону "
                  "\n2 - Добавить запись в телефонную книгу "
                  "\n3 - Удаление запись из телефонной книги "
                  "\n4-  Экспорт в HTML "
                  "\n -> "))

    match p:
        case 1:
            data = view.Input_tel()
            st = database.read_from_file()
            lst = funcs.Convert_str_to_list(st)
            rez = funcs.search_phone(data, lst)
            view.print_data(rez)
        case 2:
            a,b,c,d = funcs.Add_data()
            database.write_to_txt(a,b,c,d)
            database.write_to_csv(a,b,c,d)
        case 3:
            st = database.read_from_file()
            view.print_data(st)
            data = view.Input_tel()
            lst = funcs.Convert_str_to_list(st)
            view.print_data(lst)
            rez = funcs.Delete_phone(data, lst)
            view.print_data(rez)
        case 4:
            st = database.read_from_file()
            lst = funcs.Convert_str_to_list(st)
            funcs.Import_HTML(lst)
        