from random import randint

class Coder:
    def text_to_int(text):
        coding_text = []
        for i in text:
            coding_text.append(str(ord(i)))
        return coding_text

    def convert_base(num, to_base=10, from_base=10):

        if isinstance(num, str):
            n = int(num, from_base)
        else:
            n = int(num)

        alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if n < to_base:
            return alphabet[n]
        else:
            return Coder.convert_base(n // to_base, to_base) + alphabet[n % to_base]

    def stud_cod(text: int, rand):
        x = 0
        li = []
        
        for i in rand:
            if x > 0:
                text = Coder.convert_base(text, to_base=i, from_base=rand[x-1])
            else:
                text = Coder.convert_base(text, to_base=i)
            li.append(text)
            x += 1
        return li


class Decoder:
    def int_to_text(text):
        coding_text = []
        for i in text:
            coding_text.append(chr(int(i)))
        return coding_text

    def conv_to_text(number, base):
        return [int(i, base) for i in number]
    
    def rev_cod(text, rand):
        x = 0
        li = []

        for i in rand:
            try:
                text = Coder.convert_base(text, to_base=rand[x+1], from_base=i)
            except:
                text = Coder.convert_base(text, to_base=10, from_base=i)
            li.append(text)
            x += 1
        return li


def randomer():
    li = []
    for i in range(randint(3, 15)):
        li.append(randint(2, 36))
    return li

ua = {
    "cod": "Кодувати",
    "dec": "Декодувати",
    "inf": "Про програму",
    "dov": "Довідка",
    "switch_1": "Темна тема",
    "menu1": "Новий                 Ctrl+N",
    "menu2": "Відкрити             Ctrl+O",
    "menu3": "Зберегти             Ctrl+S",
    "menu4": "Зберегти як",
    "menu5": "Розмір шрифта",
    "menu_format": "Формат",
    "menu_nam": "Файл",
    "font_question": "Введіть розмір шрифту:",
    "font_title": "Розмір шрифту"
}
en = {
    "cod": "Encode",
    "dec": "Decode",
    "inf": "About program",
    "dov": "Certificate",
    "switch_1": "Dark theme",
    "menu1": "New                Ctrl+N",
    "menu2": "Open              Ctrl+O",
    "menu3": "Save                Ctrl+S",
    "menu4": "Save as",
    "menu5": "Font size",
    "menu_format": "Format",
    "menu_nam": "File",
    "font_question": "Enter the font size:",
    "font_title": "Font size"
}
