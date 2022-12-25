from tkinter import *
from tkinter import ttk

import database
import funcs

data = ''
languages = ["Python", "JavaScript", "C#", "Java"]

main_window = Tk()
main_window.title("Приложение на Tkinter")
main_window.geometry("600x650")

label = Label(text=data)  # создаем текстовую метку
label.pack()  # размещаем метку в окне


def click_search_btn():
    global data
    data = 'hi world'
    label['text'] = data


def print_handbook():
    global data
    global languages
    data = str(funcs.get_data_from_bd(database.read_from_file()))
    languages = str(funcs.get_data_from_bd(database.read_from_file()))
    label['text'] = data
    languages_var = Variable(value=languages)
    languages_listbox['listvariable'] = languages_var


# search
search_btn = ttk.Button(text='поиск', command=click_search_btn)
# command=controller.search_by_info())
search_btn.pack(anchor=CENTER, expand=1)

print_btn = ttk.Button(text='распечатать спарвочник', command=print_handbook)
print_btn.pack(anchor=CENTER, expand=1)

languages_var = Variable(value=languages)

languages_listbox = Listbox(listvariable=languages_var)
languages_listbox.pack(anchor=NW, fill=X, padx=5, pady=5)

main_window.mainloop()
