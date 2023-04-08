from tkinter import *
from tkinter import filedialog

from customtkinter import *

import os
import base64
import configparser

from conf import *


def keys(event):
    if event.keycode==79:
        open_file()
    if event.keycode==78:
        new_file()
    if event.keycode==83:
        save_file()

def decode_file(text):
    dec = base64.b64decode(text).decode("UTF-8")
    dec = eval(base64.b16decode(dec).decode("UTF-8"))

    c = dec[0]
    c.reverse()

    x = [Decoder.rev_cod(i[-1], c) for i in dec[1]]
    dec_int = [i[-1] for i in x]

    text1.delete('1.0', END)
    text1.insert('1.0', "".join(Decoder.int_to_text(dec_int)))

def code_file(text):
    global comp

    interim = []
    rand = randomer()

    tint = Coder.text_to_int(text)
    coding_text = [Coder.stud_cod(i, rand) for i in tint]
    interim.append(rand)
    interim.append(coding_text)
    comp = base64.b16encode(str(interim).encode("UTF-8")).decode("UTF-8")


def open_file():
    try:
        file = open(filedialog.askopenfilename(parent=notep, filetypes=[("Text Documents", "*.txt")]),
                    'r', encoding='utf-8')
        decode = file.read()

        title = os.path.basename(file.name)
        notep.title(title + " - Notepad++")

        try:
            decode_file(decode)
        except:
            text1.delete('1.0', END)
            text1.insert('1.0', decode)

        file.close()
    except:
        pass

def save_file():
    try:
        code_file(text1.get('1.0', END))

        with open(filedialog.asksaveasfilename(defaultextension=".txt",
                filetypes=[("Text Documents", "*.txt")]), 'w', 
                encoding='utf-8') as file_save:

            if file_save is None:
                return

            file_save.write(base64.b64encode(str(comp).encode("UTF-8")).decode("UTF-8"))
            # file_save.write(" ")
            # file_save.write(base64.b64encode("".join(str(coding_text)).encode("UTF-8")).decode("UTF-8"))
            file_save.close()
    except:
        pass

def save_org_text():
    try:
        with open(filedialog.asksaveasfilename(defaultextension=".txt",
                filetypes=[("Text Documents", "*.txt")]), 'w', 
                encoding='utf-8') as file_save:

            if file_save is None:
                return

            file_save.write(text1.get('1.0', END))
            file_save.close()
    except:
        pass

def new_file():
    notep.title("Notepad++")
    
    text1.delete('1.0', END)

def select_temp():
    if switch_var.get() == "on":
        set_appearance_mode("dark")
        config.set('theme', 'theme', "dark")
        config.set('var', 'switch_var', "on")
    else:
        set_appearance_mode("light")
        config.set('theme', 'theme', "light")
        config.set('var', 'switch_var', "off")

    with open(r"conf.ini", 'w') as configfile:
        config.write(configfile)

def select_lang(choice):
    global lang
    lang = choice

    config.set('language', 'language', choice)

    if choice == "Українська":
        cod_text.set(value=ua["cod"])
        dec_text.set(value=ua["dec"])
        inf_text.set(value=ua["inf"])
        dov_text.set(value=ua["dov"])
        switch_1_text.set(value=ua["switch_1"])
        config.set('var', 'langmenu_var', choice)
    else:
        cod_text.set(value=en["cod"])
        dec_text.set(value=en["dec"])
        inf_text.set(value=en["inf"])
        dov_text.set(value=en["dov"])
        switch_1_text.set(value=en["switch_1"])
        config.set('var', 'langmenu_var', choice)

    with open(r"conf.ini", 'w') as configfile:
        config.write(configfile)

def font_sizer():
    global font
    fonte = CTkInputDialog(text=ua["font_question"] if lang == "Українська" else en["font_question"],
                          title=ua["font_title"] if lang == "Українська" else en["font_title"])
    try:
        font = int(fonte.get_input())
    except:
        font = 17

    config.set('font', 'font', str(font))
    with open(r"conf.ini", 'w') as configfile:
        config.write(configfile)

    try:
        text1.configure(font=("ubuntu", font))
        text.configure(font=("ubuntu", font))
    except:
        pass

def notepad(opn):
    global text1, notep

    notep = CTkToplevel()
    notep.geometry("900x500")
    notep.title("Notepad++")
    notep.iconbitmap('icon.ico')

    notep.focus_set()

    notep.bind("<Control-KeyPress>", keys)

    text1 = CTkTextbox(notep, height=9000, width=9000, font=("ubuntu", font), wrap="word")
    text1.pack()

    menubar = Menu(notep)

    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label=ua["menu1"] if lang == "Українська" else en["menu1"], command=new_file)
    filemenu.add_command(label=ua["menu2"] if lang == "Українська" else en["menu2"], command=open_file)
    filemenu.add_command(label=ua["menu3"] if lang == "Українська" else en["menu3"], command=save_file)
    filemenu.add_command(label=ua["menu4"] if lang == "Українська" else en["menu4"], command=save_org_text)
    menubar.add_cascade(label=ua["menu_nam"] if lang == "Українська" else en["menu_nam"], menu=filemenu)

    formatmenu = Menu(menubar, tearoff=0)
    formatmenu.add_command(label=ua["menu5"] if lang == "Українська" else en["menu5"], command=font_sizer)
    menubar.add_cascade(label=ua["menu_format"] if lang == "Українська" else en["menu_format"], menu=formatmenu)
    
    notep.config(menu=menubar)
    
    if opn:
        open_file()

    notep.mainloop()

def info(opn):
    global text
    infor = CTkToplevel()
    infor.geometry("900x500")
    infor.title("Notepad++ - information")
    infor.iconbitmap('icon.ico')

    text = CTkTextbox(infor, height=9000, width=9000, font=("ubuntu", font), wrap="word")
    text.pack()

    if opn:
        if lang == "Українська":
            f = open(f"{os.getcwd()}\\info\\ua_info.txt", "r", encoding='utf-8')
        else:
            f = open(f"{os.getcwd()}\\info\\en_info.txt", "r", encoding='utf-8')
    else:
        if lang == "Українська":
            f = open(f"{os.getcwd()}\\info\\ua_about.txt", "r", encoding='utf-8')
        else:
            f = open(f"{os.getcwd()}\\info\\en_about.txt", "r", encoding='utf-8')

    ff = f.read()
    text.delete('1.0', END)
    text.insert('1.0', ff)
    
    infor.mainloop()

def configini():
    config.add_section('language')
    config.set('language', 'language', 'English')

    config.add_section('font')
    config.set('font', 'font', '17')

    config.add_section('theme')
    config.set('theme', 'theme', 'dark')
    
    config.add_section('var')
    config.set('var', 'switch_var', 'on')
    config.set('var', 'langmenu_var', 'English')

    with open(r"conf.ini", 'w') as configfile:
        config.write(configfile)

config = configparser.ConfigParser()

if os.path.isfile("conf.ini"):
    pass
else:
    configini()

config.readfp(open(r'conf.ini'))

set_appearance_mode(config.get('theme', 'theme'))
set_default_color_theme("green")


lang = config.get('language', 'language')
font = int(config.get('font', 'font'))


root = CTk()
root.geometry("804x454")
root.title("Notepad++")
root.iconbitmap('icon.ico')
root.resizable(False, False)


root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure((0, 4, 2), weight=1)


switch_var = StringVar(value=config.get('var', 'switch_var'))
langmenu_var = StringVar(value=config.get('var', 'langmenu_var'))

bg = PhotoImage(file="bg.png")

fon = Label(root, image=bg)
fon.place(x=0, y=0)

frame = CTkFrame(master=root, width=140, corner_radius=0)
frame.grid(row=0, column=0, rowspan=6, sticky="nsew")
frame.grid_rowconfigure(4, weight=1)


cod_text = StringVar(value=ua["cod"] if lang == "Українська" else en["cod"])
dec_text = StringVar(value=ua["dec"] if lang == "Українська" else en["dec"])
inf_text = StringVar(value=ua["inf"] if lang == "Українська" else en["inf"] )
dov_text = StringVar(value=ua["dov"] if lang == "Українська" else en["dov"])
switch_1_text = StringVar(value=ua["switch_1"] if lang == "Українська" else en["switch_1"])


cod = CTkButton(root, textvariable=cod_text, font=("ubuntu", 17), command=lambda:notepad(False)).grid(row=0, column=0, padx=20, pady=(10, 0))
dec = CTkButton(root, textvariable=dec_text, font=("ubuntu", 17), command=lambda:notepad(True)).grid(row=1, column=0)
inf = CTkButton(root, textvariable=inf_text, font=("ubuntu", 17), command=lambda:info(True)).grid(row=2, column=0)
dov = CTkButton(root, textvariable=dov_text, font=("ubuntu", 17), command=lambda:info(False)).grid(row=3, column=0)

switch_1 = CTkSwitch(master=root, textvariable=switch_1_text, command=select_temp,
                     variable=switch_var, font=("ubuntu", 17), onvalue="on", offvalue="off")
switch_1.grid(row=4, column=0, pady=(100, 0))

langbox = CTkOptionMenu(master=root,
                         values=["Українська", "English"],
                         command=select_lang,
                         variable=langmenu_var,
                         font=("ubuntu", 17))
langbox.grid(row=5, column=0, pady=(0, 70))



if __name__ == '__main__':
    root.mainloop()
