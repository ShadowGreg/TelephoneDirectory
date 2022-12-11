

def Write_PB(st:str):
    with open("bp.csv","a") as data:
        data.write(st)

def Read_PB():
    with open("bp.csv","r") as data:
        st = data.read()
    return st