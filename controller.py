import database
import view
import funcs


def choose_an_action():
    flag = True
    while flag:
        p = int(input("Выберите - что хотите сделать: "
                      "\n1 - Поиск по телефону "                      
                      "\n3 - Добавить запись в телефонную книгу "
                      "\n4 - Поиск по телефону "
                      "\n5 - Удаление запись из телефонной книги "
                      "\n6 - Выход "))
        match p:
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
                flag = False
