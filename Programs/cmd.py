from tkinter import *
import os

window = Tk()

global command
command = Text(window,width=500, height=1, fg="white", background="black")
command.place(x=0, y=0)

def write():
    comd = command.get("1.0", "end-1c")
    if "delete" in comd :
        comd = comd.split("delete ")
        try:
            os.remove(f"file/{comd[1]}")
        except:
            print("Invalid File")
    elif "create" in comd:
        comd = comd.split("create ")
        comd = comd[1].split(" ")
        sets = comd[0]
        namee = comd[1].split("\"")
        name2 = namee[1]
        try:
            with open(f"file/{name2}.{comd[0]}", "x") as f:
                pass
        except:
            print("File already exists.")
        
    elif "editText" in comd:
        comd = comd.split("editText ")
        comd = comd[1].split(" ")
        sett = comd[1].split("\"")
        text = sett[1]
        file = comd[0]
        try:
            with open(f"file/{file}", "w") as f:
                f.write(text)
        except:
            print("Invalid File")
    elif "addText" in comd:
        comd = comd.split("addText ")
        comd = comd[1].split(" ")
        sett = comd[1].split("\"")
        text = sett[1]
        file = comd[0]
        try:
            with open(f"file/{file}", "a") as f:
                f.write(text)
        except:
            print("Invalid File")
            
            
submit = Button(window, fg="Red", background="black", text="Run >_", command=write)
submit.place(x=230, y=20)

window.configure(background="black")
window.title("Command Prompt")
window.geometry("500x420")
