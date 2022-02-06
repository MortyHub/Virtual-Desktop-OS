from tkinter import *
import random

# Creates window
window = Tk()
window.title("Notepad")

def Savee():
    # Gets value of every text box
    textt = Tet.get("1.0", "end-1c")
    extension = fileEx.get("1.0", "end-1c")
    name = Name.get("1.0", "end-1c")

    # Tries to create file, if file already exists then it will create the file with a random number attached to it
    try:
        with open(f"file/{name}.{extension}", "x") as f:
            f.write(textt)
    except:
        with open(f"file/{name}({str(random.randrange(1,1000))}).{extension}", "x") as f:
            f.write(textt)

# Notepad text area
Tet = Text(window, height=200, width=200, font=("Times New Roman", 10))
Tet.place(x=0,y=55)

# This is the Save As Button
Save = Button(window, text="Save As", fg="Red", font=("Times New Roman", 15), command=Savee)
Save.place(x=0, y=0)

# File extension text box
fileEx = Text(window, height=1, width=25, font=("Times New Roman", 14))
fileEx.place(x=180,y=0)

# Text box where they input the name of the name
Name = Text(window, height=1, width=25, font=("Times New Roman", 14))
Name.place(x=180, y=27)

window.attributes('-fullscreen', True)
window.mainloop()