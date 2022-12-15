from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
import datetime
import os

root = Tk()
root.title("Untitled - Notepad")
root.configure(bg="black")
root.geometry("600x600")
#root.iconphoto("Notepad.png")

def newFile():
    global file
    root.title("Untitled - Notepad")
    entry.delete(1.0, END)
       
def openFile():
    global file
    file = askopenfilename(defaultextension = ".txt", filetype=[("Text.Documents", "*.txt")])
    if file == " ":
        file = None
        
    else:
        root.title(os.path.basename(file)  + " - Notepad")
        f = open(file, "r")
        entry.insert(1.0, f.read())
        f.close()
        
def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt"), ])
        if file == "":
            file = None
        else:
            f = open(file, "w")
            f.write(entry.get(1.0, END))  
            f.close()
            root.title(os.path.basename(file)  + " - Notepad")
    else:
            f = open(file, "w")
            f.write(entry.get(1.0, END))  
            f.close()

def saveAsFile():
    global file
    if file == None:
        file = asksaveasfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt"), ])
        if file == "":
            file = None
        else:
            f = open(file, "w")
            f.write(entry.get(1.0, END))  
            f.close()
            root.title(os.path.basename(file)  + " - Notepad")
    else:
        file = asksaveasfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt"), ])
        f = open(file, "w")
        f.write(entry.get(1.0, END))  
        f.close()
            
def cut():
    entry.event_generate(("<<Cut>>"))

    
def copy():
    entry.event_generate(("<<Copy>>"))
    
def paste():
    entry.event_generate(("<<Paste>>"))

def dateTime():
    date = str(datetime.datetime.now())
    entry.insert(1, date)

def selectAll():
    entry.event_generate(("<<Select>>"))   
            
def exitFile():
    root.destroy()

date = StringVar()

scrollbar = Scrollbar(root, width=12)

scrollbar.pack(side=RIGHT, fill=Y)
scrollbar.configure(bg="black")
entry = Text(root, wrap=WORD, bg="white", font=("Calibri",11), fg="black")
entry.pack(padx=1, pady=1, expand=TRUE, fill=BOTH)
TextArea = Text(root)
file = None
#TextArea.pack(expand="True", fill="BOTH")

MenuBar = Menu(root)
FileMenu = Menu(MenuBar, tearoff=0)
FileMenu.add_command(label="New", command=newFile)
FileMenu.add_command(label="New Window")
FileMenu.add_command(label="Open", command=openFile)
FileMenu.add_command(label="Save", command=saveFile)
FileMenu.add_command(label="Save As", command=saveAsFile)
FileMenu.add_separator()
FileMenu.add_command(label="Page Setup")
FileMenu.add_command(label="Print")
FileMenu.add_separator()
FileMenu.add_command(label="Exit", command=exitFile)


EditMenu = Menu(MenuBar, tearoff=0)
EditMenu.add_command(label="Undo")
EditMenu.add_separator()
EditMenu.add_command(label="Cut", command=cut)
EditMenu.add_command(label="Copy", command=copy)
EditMenu.add_command(label="Paste", command=paste)
EditMenu.add_command(label="Delete")
EditMenu.add_separator()
EditMenu.add_command(label="Find")
EditMenu.add_command(label="Find next")
EditMenu.add_command(label="Find previous")
EditMenu.add_command(label="Replace")
EditMenu.add_command(label="Go to")
EditMenu.add_separator()
EditMenu.add_command(label="Select all", command=selectAll)
EditMenu.add_command(label="Time/Date", command=dateTime)
EditMenu.add_separator()
EditMenu.add_command(label="Font")


ViewMenu = Menu(MenuBar, tearoff=0)
ViewMenu.add_command(label="Zoom")
ViewMenu.add_command(label="Status bar")
ViewMenu.add_command(label="Word wrap")


MenuBar.add_cascade(label="File", menu=FileMenu)
MenuBar.add_cascade(label="Edit", menu=EditMenu)
MenuBar.add_cascade(label="View", menu=ViewMenu)


root.config(menu=MenuBar)
root.mainloop()