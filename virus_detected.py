from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry("200x200")

def warning():
    messagebox.showwarning("Alert!","Stop! virus found.")
btn = Button(root,text="scan for virus",command=warning)
btn.pack()

def error():
    messagebox.showerror("Error!","404 not found")
btn1 = Button(root,text="see for error",command=error)
btn1.pack()

def yesorno():
    messagebox.askyesno("Confirmation","Are you sure u want to continue?")
question = Button(root,text="check",command=yesorno)
question.pack()

root.mainloop()

