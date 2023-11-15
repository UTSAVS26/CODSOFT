from tkinter import *
import random, string

root = Tk()
root.geometry("400x280")
root.title("Password Generator")

title = StringVar()
label = Label(root, textvariable = title, font = ("Comic Sans MS", 15)).pack()
title.set("The strength of our password:")

def selection():
    selection = choice.get()

choice = IntVar()
R1 = Radiobutton(root, text = "POOR", font = ("Comic Sans MS", 10), variable = choice, value = 1, command = selection).pack(anchor = CENTER)
R2 = Radiobutton(root, text = "AVERAGE", font = ("Comic Sans MS", 10), variable = choice, value = 2, command = selection).pack(anchor = CENTER)
R3 = Radiobutton(root, text = "ADVANCED", font = ("Comic Sans MS", 10), variable = choice, value = 3, command = selection).pack(anchor = CENTER)
labelchoice = Label(root)
labelchoice.pack()

lenlabel = StringVar()
lenlabel.set("Password length:")
lentitle = Label(root, textvariable = lenlabel, font = ("Arial", 20)).pack()

val = IntVar()
spinlenght = Spinbox(root, from_ = 8, to_ = 24, textvariable = val, font = ("Comic Sans MS", 10), width = 13).pack()

def callback():
    lsum.config(text=passgen())

# Button
passgenButton = Button(root, text = "Generate Password", font = ("Arial", 10), bd = 5, height = 2, command = callback, pady = 3)
passgenButton.pack()
password = str(callback)

# Password Result Message
lsum = Label(root, text = "",font = ("Comic Sans MS", 15))
lsum.pack(side = BOTTOM)

# Function
poor = string.ascii_uppercase + string.ascii_lowercase
average = string.ascii_uppercase + string.ascii_lowercase + string.digits
symbols = """`~!@#$%^&*()_-+={}[]\|:;"'<>,.?/"""
advance = poor + average + symbols

def passgen():
    if choice.get() == 1:
        return "".join(random.sample(poor, val.get()))
    elif choice.get() == 2:
        return "".join(random.sample(average, val.get()))
    elif choice.get() == 3:
        return "".join(random.sample(advance, val.get()))

root.mainloop()