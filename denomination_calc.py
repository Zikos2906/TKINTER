from tkinter import *
from tkinter import messagebox

window = Tk()

window.title("Denomination Calculater")
window.geometry("650x400")
window.configure(bg="light blue")
label1 = Label(window,text="hey user! welcome to denomination calculator application",bg="lightblue")
label1.place(relx=0.5,y=340,anchor=CENTER)

def msg ():
    msgbox = messagebox.showinfo("alert","Do you want to calculate the denomination count?")
    if messagebox == "ok":
        topwin() 
btn1 = Button(window,text="Lets get started",command=msg,bg="brown",fg="white")
btn1.place(x=260,y=360)

def topwin ():
    top = Toplevel()
    top.title("Denomination calculator")
    top.geometry("500x300")
    top.configure(bg="light grey")
    l = Label(top,text="Enter total amount",bg="light grey")
    entry = Entry(top)
    lbl = Label(top,text="Here are the number of notes for each denomination: ",bg="light grey")
    l1 = Label(top,text="2000",bg="light grey")
    l2 = Label(top,text="500",bg="light grey")
    l3 = Label(top,text="100",bg="light grey")
    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)
    def calculator():
        try:
            amount = int(entry.get())
            note2000 = amount//2000
            amount %= 2000
            note500 = amount//500
            amount %= 500
            note100 = amount//100
            t1.delete(0,END)
            t2.delete(0,END)
            t3.delete(0,END)
            t1.insert(END,str(note2000))
            t2.insert(END,str(note500))
            t3.insert(END,str(note100))
        except ValueError:
            messagebox.showerror("Error!","Please enter a valid number!")
    btn = Button(top,text="Calculate",command=calculator,bg="red",fg="white")
    l = 