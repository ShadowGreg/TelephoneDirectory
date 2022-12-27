#Запросы проверок:
check_table_phones_exist = """SELECT count(*) FROM sqlite_master WHERE type='table' AND name='phones';"""

#создание таблицы
create_table_phones="""CREATE TABLE phones(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        first_name TEXT NOT NULL,
                        last_name TEXT NOT NULL,
                        phone_number TEXT NOT NULL,
                        comment TEXT NOT NULL
                        );"""
                        
#Добавление и удаление записей
add_contact = """INSERT INTO phones (first_name, last_name, phone_number, comment) VALUES = (?, ?, ?, ?)"""
delete_contact = """DELETE FROM phones WHERE id = ?""" 


#Поиск записей

#Выбор всех записей
all_records = """SELECT * FROM phones"""
p_num_search = """SELECT * FROM phones WHERE phone_number = ?"""
