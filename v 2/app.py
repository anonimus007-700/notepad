from tkinter import *
from tkinter import filedialog

from customtkinter import *

import os
import base64

from conf import *

set_appearance_mode("dark")  # Modes: system (default), light, dark
set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

root = CTk()
root.geometry("900x500")
root.title("Notepad++")
root.iconbitmap('icon.ico')


def keys(event):
    if event.keycode==79:
        open_file()
    if event.keycode==78:
        new_file()
    if event.keycode==83:
        save_file()

def decode_file(text):
    decode = text.split(" ")

    dec = eval(base64.b64decode(decode[0]).decode("UTF-8"))
    dec.reverse()
    decode.pop(0)
    cod_text = eval(base64.b64decode(decode[0]).decode("UTF-8"))

    x = [Decoder.rev_cod(i[-1], dec) for i in cod_text]
    dec_int = [i[-1] for i in x]

    text1.delete('1.0', END)
    text1.insert('1.0', "".join(Decoder.int_to_text(dec_int)))

def code_file(text):
    global coding_text, rand

    rand = randomer()

    tint = Coder.text_to_int(text)
    coding_text = [Coder.stud_cod(i, rand) for i in tint]


def open_file():
    file = open(filedialog.askopenfilename(filetypes=[("Text Documents", "*.txt")]),
                'r', encoding='utf-8')
    decode = file.read()

    title = os.path.basename(file.name)
    root.title(title + " - Notepad++")

    try:
        decode_file(decode)
    except:
        text1.delete('1.0', END)
        text1.insert('1.0', decode)

    file.close()

def save_file():
    try:
        code_file(text1.get('1.0', END))

        with open(filedialog.asksaveasfilename(defaultextension=".txt",
                filetypes=[("Text Documents", "*.txt")]), 'w', 
                encoding='utf-8') as file_save:

            if file_save is None:
                return

            file_save.write(base64.b64encode(str(rand).encode("UTF-8")).decode("UTF-8"))
            file_save.write(" ")
            file_save.write(base64.b64encode("".join(str(coding_text)).encode("UTF-8")).decode("UTF-8"))
            file_save.close()
    except:
        pass

def new_file():
    root.title("Notepad++")
    
    text1.delete('1.0', END)


root.bind("<Control-KeyPress>", keys)

text1 = CTkTextbox(root, height=9000, width=9000, font=("ubuntu", 14))
text1.pack()

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New...               Ctrl+N", command=new_file)
filemenu.add_command(label="Open                Ctrl+O", command=open_file)
filemenu.add_command(label="Save                  Ctrl+S", command=save_file)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

root.config(menu=menubar)

if __name__ == '__main__':
    root.mainloop()
