from tkinter import *

window = Tk()

global command
command = Text(window,width=500, height=1, fg="white", background="black")
command.place(x=0, y=0)

def write():
    print(command.get("1.0", "end-1c"))

submit = Button(window, fg="Red", background="black", text="Run >_", command=write)
submit.place(x=230, y=20)

window.configure(background="black")
window.title("Command Prompt")
window.geometry("500x420")