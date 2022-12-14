import database as db
import view as v
import funcs


def choose_an_action():
    flag = True
    while flag:
        p = int(input("Выберите - что хотите сделать: "
                      "\n1 - Поиск по Фамилии или Имени "                      
                      "\n3 - Добавить запись в телефонную книгу "
                      "\n4 - Поиск по телефону "
                      "\n5 - Удаление запись из телефонной книги "
                      "\n6 - Выход\n "))
        match p:
            case 1:
                pass
            case 2:
                pass
            case 3:
                db.write_to_txt(v.input_data())
                break
            case 4:
                pass
            case 5:
                pass
            case 6:
                flag = False
            

choose_an_action()