import database as db
import view as v
import funcs as f


def choose_an_action():
    flag = True
    while flag:
        p = int(input("Выберите - что хотите сделать: "
                      "\n1 - Поиск по Фамилии"
                      "\n1 - Поиск по Имени"                      
                      "\n3 - Поиск по телефону "
                      "\n4 - Поиск по комментарию "
                      "\n5 - Добавить запись в телефонную книгу "
                      "\n6 - Удаление запись из телефонной книги "
                      "\n7 - Выход\n "))
        match p:
            case 1:
                v.print_data(f.search_by_surname(v.input_surname(), f.get_data_from_bd(db.read_from_file('bp.txt'))))
                break
            case 2:
                v.print_data(f.search_by_name(v.input_name(), f.get_data_from_bd(db.read_from_file('bp.txt'))))
                break
            case 3:
                v.print_data(f.search_by_number(v.input_number(), f.get_data_from_bd(db.read_from_file('bp.txt'))))
                break
            case 4:
                v.print_data(f.search_by_comment(v.input_comment(), f.get_data_from_bd(db.read_from_file('bp.txt'))))
                break
            case 5:
                db.write_to_txt(v.input_data())
                break
            case 6:
                pass
            case 7:
                flag = False
            