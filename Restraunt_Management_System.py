import tkinter as tk
from tkinter import ttk,messagebox
menu = {"Fries":2,"Burger":3,"Pizza":3,"Pasta":3,"Sprite":2,"Ice Cream":2}
def order():
    rate = 95 if cur.get() == "INR" else 1 
    sym  = "rs" if cur.get() == "INR" else "$"
    total,txt = 0,"order summary \n"
    for item,e in entries.items():
        q = int(e.get()or 0)
        if q:
            cost = q*menu[item]*rate
            total += cost
            txt += f"{item}:{q}={sym}{cost}\n"
    messagebox.showinfo("order: ",txt+f"\ntotal {sym} {total}") if total else \
    messagebox.showerror("error","No items selected")

root = tk.Tk()
root.title("Restraunt Manager App")
entries = {}
for i, (item,price) in enumerate(menu.items()):
    ttk.Label(root,text=f"{item}(${price})").grid(row=i,column=0)
    entries[item] = ttk.Entry(root,width=5)
    entries[item].grid(row=i,column=1)
cur = tk.StringVar(value = "USD")
ttk.Combobox(root,textvariable=cur,values=["USD","INR"],state="readonly",width=10).grid(row=len(menu),column=1)
ttk.Button(root,text="order",command=order).grid(row=len(menu)+1,columnspan=2)
root.mainloop()

