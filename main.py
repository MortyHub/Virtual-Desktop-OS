from tkinter import *
from tkinter.ttk import *
import webbrowser
import subprocess
import os
import random

window = Tk()

style = Style()

placingX = 160

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
cmdIcon = PhotoImage(file = r"icons/cmd.png")

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
        os.system("python3")
    except:
        print("Error: python does not exist")

def NotepadOpen():
    exec(open("Programs/Notepad.py").read())

def openCMD():
    exec(open("Programs/cmd.py").read())

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

# CMD button

CMD = Button(window, text="e", image=cmdIcon, command=openCMD)
CMD.place(x=160, y=40)

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
    Fileb = NewFilee(newName.get("1.0", "end-1c"), newType.get("1.0", "end-1c"), newContent.get("1.0", "end-1c"))

    newFile.destroy()
    newType.destroy()
    newName.destroy()
    newContent.destroy()

def right_click(event):
    global newFile
    global newType
    global newName
    global newContent
    try:
        newFile.destroy()
        newType.destroy()
        newName.destroy()
        newContent.destroy()
    except:
        pass
    newFile = Button(window, text="New File", command=newFil)
    newName = Text(window, width=5, height=1)
    newType = Text(window, width=5, height=1)
    newContent = Text(window, width=5, height=1)
    newFile.place(x=x, y=y)
    newType.place(x=x+80, y=y)
    newName.place(x=x+80, y=y+20)
    newContent.place(x=x+80, y=y+40)


# creates new file into the file folder along with placing the file on the desktop
class NewFilee:
    def __init__(self, name, type, contents):
        self.name = name
        self.type = type
        self.contents = contents
        global placingX
        placingX += 40
        try:
            with open(f"file/{name}.{type}", "x") as f:
                print("e")
                if type == "txt":
                    self.name = Button(window, text=f"{self.name}", image=noteIcon)
                    self.name.place(x=placingX, y=40)
                elif type == "cmdl":
                    self.name = Button(window, text=f"{self.name}", image=cmdIcon, command=lambda: cmdlFile(f"{contents}"))
                    self.name.place(x=placingX, y=40)
                    print("a")
                elif type == "":
                    self.name = Button(window, text=f"{self.name}", image=blankIcon)
                    self.name.place(x=placingX, y=40)

        except:
            with open(f"file/{name}{str(random.randrange(0,1000))}.{type}", "x") as f:
                if type == "txt":
                    self.name = Button(window, text="New File", image=noteIcon)
                    self.name.place(x=placingX, y=40)
                else:
                    self.name = Button(window, text="New File", image=blankIcon)
                    self.name.place(x=placingX, y=40)

def cmdlFile(a):
    comd = a
    if("delete" in comd):
        comd = comd.split("delete ")
        try:
            os.remove(f"file/{comd[1]}")
        except:
            print("Invalid File")
    

window.bind("<Button-3>", right_click)
window.bind('<Motion>', motion)

#window.iconbitmap('icon.ico')

window.title("Desktop")
window.geometry("500x313")
window.mainloop()