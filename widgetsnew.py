from tkinter import *
from datetime import date
name = Tk()
name.title("gtiing Started")
name.geometry("400x300")

lbl = Label(text = "hey there",fg="white",bg="blue")
name_lbl = Label(text = "full name",bg="yellow")
name_entry = Entry()

def display():
    name_1 = name_entry.get()
    global message
    message = "Welcome to the application todays date is-"
    greet = "hello " + name_1
    textbox.insert(END,greet)
    textbox.insert(END,message)
    textbox.insert(END,date.today())
textbox = Text(height=3)
btn = Button(text = "begin",command=display,bg="black",fg="white")
lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
textbox.pack()
name.mainloop()