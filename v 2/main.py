from tkinter import *

from customtkinter import *


def select_temp():
    if switch_var.get() == "on":
        set_appearance_mode("dark")
    else:
        set_appearance_mode("light")


set_appearance_mode("dark")
set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green


root = CTk()
root.geometry("900x500")
root.title("Notepad++")
root.iconbitmap('icon.ico')


switch_var = StringVar(value="on")

bg = PhotoImage(file = "bg.png")

fon = Label(root, image=bg)
fon.place(x = 0, y = 0)

frame = CTkFrame(master=root, width=140, corner_radius=0)
frame.grid(row=0, column=0, rowspan=5, sticky="nsew")
frame.grid_rowconfigure(5, weight=1)

cod = CTkButton(root, text="Кодувати").grid(row=0, column=0, padx=20)
dec = CTkButton(root, text="Декодувати").grid(row=1, column=0)
inf = CTkButton(root, text="Про програму").grid(row=2, column=0)
dov = CTkButton(root, text="Довідка").grid(row=3, column=0)

switch_1 = CTkSwitch(master=root, text="Темна тема", command=select_temp,
                     variable=switch_var, onvalue="on", offvalue="off")
switch_1.grid(row=4, column=0, padx=20, pady=(10, 10))

if __name__ == '__main__':
    root.mainloop()
