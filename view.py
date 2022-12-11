def InputData():
    fio = input("Введите ФИО: ")
    tel = input("Введите номер телефона: ")
    com = input("Введите комментарий: ")
    return [fio,tel,com]

def OutputData(st):
    print(st)

def ListToStr(st):
    rez=''
    for i in st:
        rez+= i+';'
    return rez


