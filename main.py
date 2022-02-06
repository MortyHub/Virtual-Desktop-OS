from tkinter import *
from tkinter.ttk import *
import webbrowser
import subprocess
import os
import random
window = Tk()

style = Style()


bg = PhotoImage(file = r"backgrounds/winXP.png")
label = Label(
    window,
    image=bg
)
label.place(x=0, y=0)

# Image Defining
chromeIcon = PhotoImage(file = r"icons/Chromepng.png")
minIcon = PhotoImage(file = r"icons/minecraft.png")
pyIcon = PhotoImage(file = r"icons/py.png")
noteIcon = PhotoImage(file = r"icons/Notepad.png")
blankIcon = PhotoImage(file = r"icons/blank.png")

def webO():
    try:
        webbrowser.open('www.google.com', new=2)
    except:
        print("Error: An error has occurred")

def OpenMC():
    try:
        subprocess.call('C:\Program Files (x86)\Minecraft\MinecraftLauncher.exe')
    except:
        print("Error: Minecraft does not exist")

def pyOpen():
    try:
        os.system("py")
    except:
        print("Error: python does not exist")

def NotepadOpen():
    exec(open("Programs/Notepad.py").read())

# Chrome Button

chrome = Button(window, text="hi",image = chromeIcon, command=webO)
chrome.place(x=0,y=40)


# Minecraft Button
Minecraft = Button(window, text="F", image = minIcon, command=OpenMC)
Minecraft.place(x=40, y=40)

# Python button
python = Button(window, text="e", image = pyIcon, command=pyOpen)
python.place(x=80, y=40)

# Notepad Button
Notepad = Button(window, text="w", image= noteIcon, command=NotepadOpen)
Notepad.place(x=120, y=40)

# Taskbar

taskbar = Canvas(
    window,
    height=30,
    width=500,
    bg="#1e2757"
)
taskbar.pack()
def motion(event):
    global x
    global y
    x = event.x
    y = event.y

def newFil():
    Fileb = NewFilee(newName.get("1.0", "end-1c"), newType.get("1.0", "end-1c"))

    newFile.destroy()
    newType.destroy()
    newName.destroy()





def right_click(event):
    global newFile
    global newType
    global newName
    newFile = Button(window, text="New File", command=newFil)
    newType = Text(window, width=5, height=1)
    newName = Text(window, width=5, height=1)
    newFile.place(x=x, y=y)
    newType.place(x=x+80, y=y)
    newName.place(x=x+80, y=y+20)


class NewFilee:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        try:
            with open(f"file/{name}.{type}", "x") as f:
                pass
        except:
            with open(f"file/{name}{str(random.randrange(0,1000))}.{type}", "x") as f:
                pass



window.bind("<Button-3>", right_click)
window.bind('<Motion>', motion)
window.iconbitmap('icon.ico')
window.title("Desktop")
window.geometry("500x313")
window.mainloop()