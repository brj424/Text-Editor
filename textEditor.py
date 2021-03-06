from Tkinter import *

root = Tk()

screenW = root.winfo_screenwidth()
screenH = root.winfo_screenheight()

root.title("Text Editor")
root.focus_set()
root.geometry("800x600")
root.configure(background="light blue")

frameTop = Frame(root, background="light blue")
frameTop.pack(side="top")

frameBottom = Frame(root, background="light blue")
frameBottom.pack(side="bottom")

scrollbar = Scrollbar(frameBottom)
scrollbar.pack(side=RIGHT, fill=Y)

txtPaper = Text(frameBottom, wrap="word", relief="ridge", yscrollcommand=scrollbar.set, bg="white", font="Times 12", spacing1=2)
scrollbar.config(command=txtPaper.yview)

lblFileName = Label(frameTop, text="File Name to Open / Save: ", bg="light blue")

fontChoice = StringVar(root)
fontChoice.set("Times")


txtFileName = Entry(frameTop)

def changeFont(fontPicked):
    txtPaper.config(font=fontPicked)

def new():
    txtPaper.delete('1.0', END)

def openf():
    fileName = txtFileName.get()
    if fileName == "":
        lblFileName.config(fg="red")
        return
    txt = open(fileName+".txt")
    new()
    txtPaper.insert("1.0",txt.read())

def save():
    fileName = txtFileName.get()
    if fileName == "":
        lblFileName.config(fg="red")
        return
    lblFileName.config(fg="black")
    f = open(fileName+".txt", 'w')
    a = txtPaper.get("1.0",END)
    f.write(a)
    f.close()

btnNew = Button(frameTop, text="NEW", command=new, bg="white", cursor="hand2")
btnOpen = Button(frameTop,text="OPEN", command=openf, bg="white", cursor="hand2")
btnSave = Button(frameTop, text="SAVE", command=save, bg="white", cursor="hand2")

fontMenu = OptionMenu(frameTop, fontChoice, "Times", "Nyala", "Calibri", command=changeFont)

def select_all(event):
    txtPaper.tag_add(SEL, "1.0", END)
    txtPaper.mark_set(INSERT, "1.0")
    txtPaper.see(INSERT)
    return 'break'

txtPaper.bind("<Control-Key-a>", select_all)
txtPaper.bind("<Control-Key-A>", select_all)

btnNew.grid(row=1,column=1,pady=(40,0))
btnOpen.grid(row=1,column=2,padx=(20,0),pady=(40,0))
btnSave.grid(row=1,column=3,padx=(20,0),pady=(40,0))
lblFileName.grid(row=1,column=4,padx=(20,0),pady=(40,0))
txtFileName.grid(row=1,column=5,pady=(40,0))
fontMenu.grid(row=1,column=6, padx=(20,0),pady=(40,0))
txtPaper.pack()

root.mainloop()
