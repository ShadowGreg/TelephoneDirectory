
def get_data_from_bd(file_data: str) -> list[list[str]]:
    file_data = file_data.replace('-', '')
    file_data = file_data.replace(' ', '')
    file_data = file_data.replace('\n', ' ')
    lst = []
    if '  ' in file_data:
        file_data = file_data.split('  ')
        for word in file_data:
            if word != '':
                s = word.split(' ')
                lst.append(s)    
        return lst
    elif ';' in file_data:
        file_data = file_data.split('  ')
        for word in file_data:
            if word != '':
                s = word.split(';')
                lst.append(s)    
        return lst   

def search_by_number(input_number: list[str], data: list[list[str]]):
      for i in range(len(data)):
        for j in range(4):
            if input_number in data[i][j]:
                return data[i]

def search_by_surname(input_surname: str, data: list[list[str]]):
      for i in range(len(data)):
        for j in range(4):
            if input_surname in data[i][j]:
                return data[i]

def search_by_name(input_name: str, data: list[list[str]]):
      for i in range(len(data)):
        for j in range(4):
            if input_name in data[i][j]:
                return data[i]

def search_by_comment(input_comment: str, data: list[list[str]]):
      for i in range(len(data)):
        for j in range(4):
            if input_comment in data[i][j]:
                return data[i]
