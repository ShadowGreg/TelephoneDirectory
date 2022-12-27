import sqlite3
import os
from urllib.request import pathname2url
import query

dbname=os.path.join(os.path.dirname(__file__), 'phone_dir.db')

def init_db():
    try:
        dburi = 'file:{}?mode=rw'.format(pathname2url(dbname))
        conn = sqlite3.connect(dburi, uri=True, check_same_thread=False)
        print('База данных найдена. открываю')
        init_cursor = conn.cursor()
        conn.close()
    except sqlite3.OperationalError:
        # Начальная установка таблиц
        print('База данных не найдена. Создаю.')
        init_conn = sqlite3.connect(dbname)
        init_cursor = init_conn.cursor()
        init_cursor.execute(query.check_table_phones_exist)
        print(str(init_cursor.execute(query.check_table_phones_exist)))
        if init_cursor.fetchone()[0]==1 : 
             print('Таблица Phones найдена!')
        else:
            print('Таблица не найдена! Создаю!')
            init_cursor.execute(query.create_table_phones)
            print('Таблица создана!')
        init_conn.commit()
        init_conn.close()
    else:
        conn = sqlite3.connect(dbname, check_same_thread=False)
        cursor = conn.cursor()
        print('Проверка таблицы phones: ', str(cursor.execute(query.check_table_phones_exist)))
        try:
            cursor.execute(query.check_table_phones_exist)
        except sqlite3.DatabaseError as e:
            print('Таблица Phones не найдена! Создаю!', e)
            cursor.execute(query.create_tables_phones)
            print('Таблица создана!')
            cursor.Commit()
            cursor.close()




