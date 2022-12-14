import database


# TOTO add next functions
# search

def search_phone(input_phone_number: str, input_array: list) -> list:
    output_records = []
    for record_line in input_array:
        if input_phone_number in record_line[2]:
            output_records.append(record_line)
    return output_records


def add_new_line_in_bd():
    sn = input("Введите Фамилию: ")
    fn = input("Введите Имя: ")
    telephone = input("Введите номер телефона: ")
    comment = input("Введите комментарий: ")
    return fn, sn, telephone, comment


def Import_HTML(input_data: list):
    html = '<!DOCTYPE HTML>'
    html += '<html>\n  <head>\n'
    # html += '<meta charset="utf-8">'
    html += '<TITLE> Телефонная книга </TITLE>\n'
    html += '</head>\n  <body>\n <table>\n'
    html += '<tr><th> Фамилия </th><th> Имя </th><th> Телефон </th><th> Комментарий </th></tr> '
    for i in range(len(input_data)):
        html += f'<tr><th> {input_data[i][0]} </th><th> {input_data[i][1]} </th><th> {input_data[i][2]} </th><th> {input_data[i][3]} </th></tr> \n'
    html += ' </table>\n </body>\n</html>'
    with open('index.html', 'w') as page:
        page.write(html)


def Convert_str_to_list(st: str):
    print(st)
    st = st.split("\n")
    for i in range(len(st)):
        st[i] = st[i].split(';')

    return st


def delete_line_fom_bd(input_phone_number: str, input_array: list) -> list:
    for i in range(len(input_array) + 1):
        if input_array[i][2] == input_phone_number:
            input_array.pop(i)
    return input_array

# def find_name_from_number():

#     find_num = v.input_number()
#     data = db.read_from_file_txt()
#     if find_num in data:
#         print()


# find_name_from_number()
