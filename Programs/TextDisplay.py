from tkinter import *

def displayText(text):
    window = Tk()

    label = Label(window, text=f"{text}", font=("Times New Roman", 9))
    label.place(x=0,y=0)
    window.title("Notepad Text Display")