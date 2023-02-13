from tkinter import *
from tkinter import filedialog
import os

from conf import *

root = Tk()
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
    decode = text

    for key, val in code.items():
        decode = decode.replace(val, key)
    for key, val in code_lover.items():
        decode = decode.replace(val, key)
    for key, val in code_num.items():
        decode = decode.replace(val, key)
    
    text1.delete('1.0', END)
    text1.insert('1.0', decode)

def code_file(text):
    global coding_text

    coding_text = text
    for key, val in code.items():
        coding_text = coding_text.replace(key, val)
    for key, val in code_lover.items():
        coding_text = coding_text.replace(key, val)
    for key, val in code_num.items():
        coding_text = coding_text.replace(key, val)

def open_file():
    try:
        file = open(filedialog.askopenfilename(filetypes=[("Text Documents", "*.txt")]),
                    'r', encoding='utf-8')

        decode = file.read()
        decode_file(decode)

        title = os.path.basename(file.name)

        root.title(title + " - Notepad++")

        file.close()
    except:
        pass

def save_file():
    code_file(text1.get('1.0', END))

    with open(filedialog.asksaveasfilename(defaultextension=".txt",
              filetypes=[("Text Documents", "*.txt")]), 'w', 
              encoding='utf-8') as file_save:

        if file_save is None:
            return

        file_save.write(coding_text)
        file_save.close()

def new_file():
    root.title("Notepad++")
    
    text1.delete('1.0', END)


root.bind("<Control-KeyPress>", keys)

text1 = Text(root, height=200, width=300, font='ubuntu 14', bg="gray",
             fg='white', wrap=WORD, bd=0)
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
