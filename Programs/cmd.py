from tkinter import *
import os

window = Tk()

global command
command = Text(window,width=500, height=1, fg="white", background="black")
command.place(x=0, y=0)

def write(a):
    comd = a
    if("delete" in comd):
        comd = comd.split("delete ")
        try:
            os.remove(f"file/{comd[1]}")
        except:
            print("Invalid File")

submit = Button(window, fg="Red", background="black", text="Run >_", command=write(command.get("1.0", "end-1c")))
submit.place(x=230, y=20)

window.configure(background="black")
window.title("Command Prompt")
window.geometry("500x420")