from tkinter import *
from tkinter.ttk import *
import webbrowser
import subprocess
import os
import random
from Programs.TextDisplay import displayText

window = Tk()

style = Style()

placingX = 200

bg = PhotoImage(file = r"backgrounds/winXP.png")
label = Label(
    window,
    image=bg
)
label.place(x=0, y=0)

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

def openFile():
    webbrowser.open('file/', new=2)

# window icon commands 

def windIco():
    global stop
    global close
    global search
    global bar


    try:
        deleteBar()
        try:
            deleteSearchBar()
        except:
            pass
        bar = Canvas(
            window,
            height=40,
            width=195,
            bg="#1e2757"
        )
        bar.pack()
        stop = Button(window, text="Close",width=5, command=exit)
        stop.place(x=173,y=54)
        search = Button(window, text="Search", width=6, command=openSearchBar)
        search.place(x=233, y=54)
        close = Button(window,text="X", width=2, command=deleteBar)
        close.place(x=303, y=54)
    except:
        pass

def deleteBar():
    try:
        stop.destroy()
        search.destroy()
        close.destroy()
        bar.destroy()
    except:
        pass
# Taskbar

taskbar = Canvas(
    window,
    height=45,
    width=500,
    bg="#1e2757"
)
taskbar.pack()

# Image Defining
chromeIcon = PhotoImage(file = r"icons/Chromepng.png")
minIcon = PhotoImage(file = r"icons/minecraft.png")
pyIcon = PhotoImage(file = r"icons/py.png")
noteIcon = PhotoImage(file = r"icons/Notepad.png")
blankIcon = PhotoImage(file = r"icons/blank.png")
cmdIcon = PhotoImage(file = r"icons/cmd.png")
winIco = PhotoImage(file = r"icons/Icon.png")
filIcon = PhotoImage(file = r"icons/FileEx.png")

# Chrome Button
chrome = Button(window, text="hi",image = chromeIcon, command=webO)
chrome.place(x=0,y=55)

# Minecraft Button
Minecraft = Button(window, text="F", image = minIcon, command=OpenMC)
Minecraft.place(x=40, y=55)

# Python button
python = Button(window, text="e", image = pyIcon, command=pyOpen)
python.place(x=80, y=55)

# Notepad Button
Notepad = Button(window, text="w", image= noteIcon, command=NotepadOpen)
Notepad.place(x=120, y=55)

# CMD button
CMD = Button(window, text="e", image=cmdIcon, command=openCMD)
CMD.place(x=160, y=55)

# File Explorer
fileex = Button(window, text="fileEx", image=filIcon, command=openFile)
fileex.place(x=200, y=55)
# icon
icon = Button(window, text="Window", image=winIco, command=windIco)
icon.place(x=5,y=5)

def openSearchBar():
    global SearchArea
    global TextBar
    global Submit
    global exitS
    global LabelS

    try:
        stop.destroy()
        bar.destroy()
        search.destroy()
        close.destroy()

        SearchArea = Canvas(
            window,
            height=150,
            width=390, 
            bg="#808080"
        )
        SearchArea.pack()
        TextBar = Text(window, height=1, width=25)
        TextBar.place(x=150, y=130)
        LabelS = Label(window, text="File Searching Engine", font=("Times New Roman", 12))
        LabelS.place(x=155, y=80)
        Submit = Button(window, text="Search", width=6, command=openFile)
        Submit.place(x=220, y=160)
        exitS = Button(window, text="X", width=2, command=deleteSearchBar)
        exitS.place(x=413, y=50)
        
        

    except:
        pass

def deleteSearchBar():
    SearchArea.destroy()
    TextBar.destroy()
    Submit.destroy()
    LabelS.destroy()
    exitS.destroy()

def openFile():
    File = TextBar.get("1.0", "end-1c")
    File1 = File.split(".")
    if File1[1] == "cmdl":
        try:
            with open(f"file/{File}", "r") as f:
                cmdlFile(f.read())
        except:
            pass
    elif File1[1] == "txt":
        try:
            with open(f"file/{File}", "r") as f:
                displayText(f.read())
        except:
            pass
    

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
    def __init__(self, name, type, contents = ""):
        self.name = name
        self.type = type
        self.contents = contents
        global placingX
        placingX += 40
        try:
            with open(f"file/{name}.{type}", "x") as f:
                print("e")
                if type == "txt":
                    self.name = Button(window, text=f"{self.name}", image=noteIcon, command=lambda: displayText(f"{self.contents}"))
                    self.name.place(x=placingX, y=55)
                    f.write(contents)
                elif type == "cmdl":
                    self.name = Button(window, text=f"{self.name}", image=cmdIcon, command=lambda: cmdlFile(f"{self.contents}"))
                    self.name.place(x=placingX, y=55)
                    f.write(contents)
                else:
                    self.name = Button(window, text=f"{self.name}", image=blankIcon)
                    self.name.place(x=placingX, y=55)
                    f.write(contents)

        except:
            with open(f"file/{name}{str(random.randrange(0,1000))}.{type}", "x") as f:
                if type == "txt":
                    self.name = Button(window, text="New File", image=noteIcon, command=lambda: displayTest(f"{self.contents}"))
                    self.name.place(x=placingX, y=55)
                    f.write(contents)
                elif type == "cmdl":
                    self.name = Button(window, text="New File", image=cmdIcon, command=lambda: cmdlFile(f"{self.contents}"))
                    self.name.place(x=placingX, y=55)
                    f.write(contents)
                else:
                    self.name = Button(window, text="New File", image=blankIcon)
                    self.name.place(x=placingX, y=55)
                    f.write(contents)


def cmdlFile(a):
    comd = a
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
    

window.bind("<Button-3>", right_click)
window.bind('<Motion>', motion)

window.iconbitmap('icon.ico')

window.title("Desktop")
window.geometry("500x313")
window.mainloop()
