from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter import messagebox as msgbox
from tkinter import Menu
from tkinter import *
import tkinter
import string
import random
import pyperclip 

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = tkinter.Tk()

#DEF OF MENUBAR FUNCTIONS
def contact():
    msgbox.showinfo('Contact','Github: www.github.com/kamilo432')
def about():
    msgbox.showinfo('About', 'It is my first independent project in python. I hope you will like it.')

# MENUBAR
menubar = Menu(window)

# HELP MENU
help_ = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Help', menu = help_)
help_.add_command(label ='Contact', command = contact)
help_.add_command(label ='About Password Generator', command = about)
help_.add_separator()
help_.add_command(label='Quit', command=window.quit)

# DISPLAY MENU
window.config(menu = menubar)

#WINDOW SETTINGS 
window.resizable(False, False)
window.geometry("566x402")
window.configure(bg = "#FFFFFF")
window.title("Password generator by kamilo432 v1.0.0")
icon = PhotoImage(file=relative_to_assets("icon.png"))
window.iconphoto(True, icon)

#BACKGROUND
canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 402,
    width = 566,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    295.0,
    214.0,
    image=image_image_1)

#BACKGROUND OF COPY BUTTON
image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    274.0,
    304.0,
    image=image_image_2)

#BACKGROUND OF "LENGHT"
image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    175.0,
    67.0,
    image=image_image_3)

#BACKGROUND OF "GENERATE PASSWORD"
image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    394.0,
    67.0,
    image=image_image_4)

#TEXT BOX
canvas.create_text(
    72.0,
    59.0,
    anchor="nw",
    text="Lenght:",
    fill="#000000",
    font=("Inter SemiBold", 16 * -1))
image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    274.0,
    186.0,
    image=image_image_5)




#SPINBOX - LENGHT OF PASSWORD INPUT
spinbox = Spinbox(window, from_ = 6, to = 32 , bg="#EAE5E5")
spinbox.pack()
spinbox.place(x=123.0, 
    y=59.0,
    width=50.0,
    height=19.0)

#TEXT BOX WHICH DISPLAYS PASSWORD
text=Text(window,bd=0, bg="#EAE5E5",font=("Inter SemiBold", 16 * -1))
text.place(x=86.0,
y=175.0,
width=378.0,
height=25.0)

#PASSWORD COMPOSITION
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "@#$&_-()=%*:/!?+.[]'"

#GENERATE PASSWORD 
def generate():
    a=spinbox.get()
    string = lower + upper + numbers + symbols
    length = int(a)
    password = "".join(random.sample(string, length))
    text.insert(INSERT ,password)

#CLEAR TEXT(PASSWORD)
def clear():
    text.delete('1.0', 'end')

#COPY TEXT(PASSWORD)
def copy():
    passw=text.get("1.0",'end-1c')
    pyperclip.copy(passw)

#BUTTON WHICH GENERERATE PASSWORD
button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=generate)
button_2.place(
    x=309.0,
    y=42.0,
    width=172.0,
    height=49.0)

#BUTTON WHICH CLEAR TEXT(PASSWORD)
button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=clear)
button_3.place(
    x=413.0,
    y=165.0,
    width=58.0,
    height=37.0)

#BUTTON WHICH COPY
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=copy,
    relief="flat")
button_1.place(
    x=188.0,
    y=280.0,
    width=172.0,
    height=49.0)

window.mainloop()
